import boto3
import uuid


# Function to list current buckets in the account
def list_my_buckets():
    s3 = boto3.resource('s3')
    print ("Here's a list of all buckets in the " + current_region + " region: \n")
    for bucket in s3.buckets.all():
        print(bucket.name)

# Create boto3 resource
s3 = boto3.resource('s3')

# Status message
print("Creating a new bucket...\n")

# Specify the bucket prefix to the value you wish to use
bucket_prefix = "bucket-for-marcus-"

# Create a function to create a new uniquely named bucket appended using the universal Unique Identifier (uuid) library - Source: https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/#:~:text=UUID%2C%20Universal%20Unique%20Identifier%2C%20is,to%20generate%20unique%20random%20id.
def create_bucket_name(bucket_prefix):
    #create unique bucket name
    return ''.join([bucket_prefix, str(uuid.uuid4())])

# Create a boto3 session
session = boto3.session.Session()

# Obtain the region from the boto3 session
current_region = session.region_name

# Set the bucket name based on the prefix and function to get a uuid
bucket_name = create_bucket_name(bucket_prefix)

# Create the bucket based on the region as some properties are not required in us-east-1
if current_region == 'us-east-1':   
    s3.create_bucket(Bucket=bucket_name)
else:
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
      'LocationConstraint': current_region})

# Print the new bucket name and region it is located in
print("New bucket name: " + bucket_name )
print("Bucket Region: " + current_region + " \n")

# List all bucket in the current region
list_my_buckets()
