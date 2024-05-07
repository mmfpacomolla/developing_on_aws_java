import boto3
import json
website_bucket = 'app-website-3f09844a-bf97-48e0-b2db-1a57339c972b'
errorFile = r'error.html'
indexFile = r'index.html'


s3 = boto3.client('s3')
bucket_name = 'app-website-3f09844a-bf97-48e0-b2db-1a57339c972b'
bucket_policy = {
     'Version': '2012-10-17',
     'Statement': [{
         'Sid': 'AddPerm',
         'Effect': 'Allow',
         'Principal': '*',
         'Action': ['s3:GetObject'],
         'Resource': "arn:aws:s3:::%s/*" % bucket_name
      }]
 }
bucket_policy = json.dumps(bucket_policy)
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)



# Enable web hosting
s3 = boto3.client('s3')
s3.put_bucket_website(
     Bucket=bucket_name,
     WebsiteConfiguration={
     'ErrorDocument': {'Key': 'error.html'},
     'IndexDocument': {'Suffix': 'index.html'},
    }
 )

# Upload html files to bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('app-website-3f09844a-bf97-48e0-b2db-1a57339c972b')
bucket.upload_file(
    'index.html', 'index.html', ExtraArgs={'ContentType': 'text/html'})
bucket.upload_file(
    'error.html', 'error.html', ExtraArgs={'ContentType': 'text/html'})


# Enable cors

s3 =boto3.client('s3')

cors_configruation = {
    'CORSRules': [{'AllowedHeaders': ['Authorization'], 'AllowedMethods': ['GET', 'PUT'], 'AllowedOrigins': ['*'], 'ExposeHeaders': ['GET', 'PUT'], 'MaxAgeSeconds': 3000}]
}

# Apply CORS configuration
s3.put_bucket_cors(Bucket=bucket_name, CORSConfiguration=cors_configruation)