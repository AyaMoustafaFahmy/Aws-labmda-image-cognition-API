import boto3
import json
from botocore.exceptions import ClientError

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('Images')

#Dynamodb Stream Trigger
def get_label_callback(event, context):
    print(event)
    id = event['Records'][0]['dynamodb']['Keys']['id']['S']
    # print(event['Records'][0])
    data = table.get_item(Key= {'id':id})
    labels = data['Item']
    print(data)
    return labels

#get data from get request 
def get_label(event,context):
    id = event['pathParameters']['id']
    
    print(event['pathParameters']['id'])
    try:
        data = table.get_item(Key= {'id':id})
        labels = data['Item']
        print("hi")
        return {
                "status": 200,
                "data": labels,
                "message": "This is an image recognition labels"
                }
    except KeyError:
        return{
            "status":404,
            "message":"Labels Not Found ,Please Check ID"
        }
        
        

