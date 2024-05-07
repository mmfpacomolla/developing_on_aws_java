# Import the modules
import boto3
from smart_open import smart_open

# Create variable to store binary data
bucket_name = 'mybucket-yc-75135'
data = '''UserId,NoteId,Notes
testuser,001,hello
testuser,002,this is my first note
student,001,DynamoDB is NoSQL
student,002,A DynamoDB table is schemaless
student,003,PartQL is a SQL compatible language for DynamoDB
student,004,I love DyDB
student,005,Maximum size of an item is ____ KB ?
newbie,001,Free swag code: 1234
newbie,002,I love DynamoDB'''

# Create boto3 resource
s3 = boto3.resource('s3')

# Create s3 object and store it in the new bucket
object = s3.Object(bucket_name, 'notes.csv')

# Store 
object.put(Body=data)

# Write out content of text file
for line in smart_open('s3://' + bucket_name + '/notes.csv', 'rb'):
    print(line.decode('utf8'))
    
