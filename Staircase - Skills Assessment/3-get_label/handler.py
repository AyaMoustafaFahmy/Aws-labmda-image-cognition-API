import boto3
import json

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('Images')

#Dynamodb Stream Trigger
def get_label_callback(event, context):
    id = event['Records'][0]['dynamodb']['NewImage']['id']['S']
    # print(event['Records'][0])
    data = table.get_item(Key= {'id':id})
    labels = data['Item']
    return labels

#get data from get request 
def get_label(event,context):
    id = event['pathParameters']['id']
    
    print(event['pathParameters']['id'])
    data = table.get_item(Key= {'id':id})
    labels = data['Item']
    print("hi")
    return labels
    
    
