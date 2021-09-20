import boto3 
import json 
from decimal import Decimal
from boto3.dynamodb.conditions import Key
import decimal
import uuid
import os

s3 = boto3.client('s3')
rekognition_client = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')


# Get Image  from S3 Bucket And send to AWS-Rekognition function
def image_recognition(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key =  event['Records'][0]['s3']['object']['key']
    filename, file_extension = os.path.splitext(key)
    
    extentions=[".jpg",".png",".jpeg",".JPG"]
    while True:
        for exten in extentions:
            if file_extension == exten:
                image_object = boto3.resource('s3').Object(bucket, key)
                try:
                    response = rekognition_client.detect_labels(Image ={'S3Object': {
                                                                'Bucket': image_object.bucket_name,
                                                                'Name': image_object.key},},
                                                                MaxLabels=5,
                                                                MinConfidence=70)
                except rekognition_client.exceptions.InvalidImageFormatException:
                    print("file is not an image or image might be corrupted")
                    break
                                                            
                image_name = image_object.key
                print('Detected labels for ' + image_object.key)
                full_labels = response['Labels']
        
                data = get_labels(full_labels)
                print(data)
                store_label(image_name,data)
                break
            
            else:
                continue
            print("please check the file you uploaded must be an image")
        break


# Store the labels in Dynamodb "images" table with a unique id
def store_label(photo_name ,labels):
    table = dynamodb.Table('Images')
    id = str(uuid.uuid4())
    data={
            "id": id,
            'photo_name':photo_name,
            'labels': labels
        }
    response = table.put_item(Item = data)
    print("data successfully added...")
    return response


# do array of lists for labels 
def get_labels(labels):
    data= {}
    data['labels']=[]
    for label in labels:
        # print (label)
        confidence = Decimal(label["Confidence"])
        name = label['Name']
        data["labels"].append({ "label": name ,"confidence" : confidence})
    return data['labels']
    
  
        # float types are not supported. Use Decimal types instead.
    # ddb_data = json.loads(json.dumps(data), parse_float=Decimal)
   
