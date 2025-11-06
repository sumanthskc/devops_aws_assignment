import boto3
import json


table_name = "Emp_Id"

# Create the DynamoDB resource
dynamo = boto3.resource('dynamodb').Table(table_name)

# Emp_Id, First_Name, Last_Name, Date_Of_Joining

def create(payload):
    return dynamo.put_item({
        "Emp_ID":payload['Emp_ID'],
        "First_Name":payload['First_Name'],
        "Last_Name":payload["Last_Name"],
        "Date_Of_Joining":payload["Date_Of_joining"]
        })
def get_item(payload):
    return dynamo.get_item(
        {
            "Emp_Id":payload['Emp_ID']
        }
    )
    
def lambda_handler(event, context):
    payload = event['payload']
    if (context.httpMethod=="post"):
           return {
               "body":json.dumps(create(payload)),
               "message":"success"
           }
    if (context.httpMethod=="get"):
        return {
               "body":json.dumps(get_item(payload)),
               "message":"success"
           }