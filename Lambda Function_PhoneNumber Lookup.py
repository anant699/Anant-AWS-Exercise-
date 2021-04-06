import boto3
import json

tableName = 'data-dip-table'

dynamodb =boto3.resource('dynamodb')

def lambda_handler(event, context):
print("Lambda trigger event:" +json.dumps(event))
    
    #handle errors in try catch block
try:
        #get the customers phone number from the event JSON
phoneNumber =event['Details']['ContactData']['CustomerEndpoint']['Address']
print ("Customer Phone number:" + Phone_Number)
    
    #init the boto3 resource to our dynamodb table
table =dynamodb.Table(tableName)
    
    #read from dynamodb
response =table.get_item(key={'Phone_Number':Phone_Number})
print("dynamodb response:"+json.dumps(response))

#if a match was found
if 'Item' in response:
print("phone number match found!")
    
    #extract the vanity number from dynamodb response
Vanity_Number=response['Item'] ['Vanity_Number']
print ("Product Vanity Number:" + Vanity_Number)
     
    #if no match found
else:
print("Phone number was not found")

expect Exception as e:
print ("An error occured while reading the database")
print(e)
return {'Vanity_Number'}
