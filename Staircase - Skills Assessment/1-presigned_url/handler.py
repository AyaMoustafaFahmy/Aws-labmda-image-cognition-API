import boto3
import json
import os

s3_client = boto3.client('s3')

#presigned url for access data in the s3 bucket 
def presigned_url(event, context):

    temp=event['body'].replace("\r\n","")
    temp=temp.replace(" ","")

    x = temp.find(":")
    y=len(temp)
    key =temp[x+2:y-2]
    
    client_method="get_object"
    response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': os.environ["BUCKET_NAME"],
                                                            'Key': key},
                                                    ExpiresIn=3600)

    print(response)
                            
    return response
    
    
#presigned url to put data in the s3 bucket    
def presigned_url_post(event, context):
    # print(event)
    client_method="put_object"
    temp=event['body'].replace("\r\n","")

    temp=temp.replace(" ","")
    x = temp.find(":")
    
    y=len(temp)
    key =temp[x+2:y-2]

    # bucket_name="image-recognition-assessment"
    params={'Bucket': "image-recognition-assessment", 'Key': key}
    response = s3_client.generate_presigned_url(client_method,params,
                                                     ExpiresIn=3600)
    return response
