# Import the modules
import boto3, json, csv
from smart_open import smart_open


# Create variable to pull binary data from your bucket
bucket_name = 'replace-with-your-bucket-name'

# Initialize data variable
data = "" 

csvFilePath = r'notes.csv'
jsonFilePath = r'notes.json'

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

# Read in each line from the  notes.csv in S3
for line in smart_open('s3://' + bucket_name + '/notes.csv', 'rb'):
    data+=(line.decode('utf8'))
    
# Verify data copied over correctly
print('Here is the value for data\n' + data)   

# Write contents to a local notes.csv file
file = open('notes.csv', 'w+')
file.write(data)
file.close()

# Run function to covert csv vile to json
csv_to_json(csvFilePath, jsonFilePath)

# Create s3 client
s3_client = boto3.client('s3')

#Upload local notes.csv file to the S3 bucket 
response = s3_client.upload_file(jsonFilePath, bucket_name, jsonFilePath)