import boto3
import json
import os
from botocore.exceptions import ClientError


s3_client = boto3.client('s3')


#presigned url for access data in the s3 bucket 
def presigned_url(event, context):
    print(event)
    client_method="get_object"
    body=json.loads(event['body'])
    key = body['image_name']
    try:
        s3_object = s3_client.get_object(Bucket=os.environ["BUCKET_NAME"], Key=key)
        response = s3_client.generate_presigned_url('get_object',
                                                Params={'Bucket': os.environ["BUCKET_NAME"],
                                                        'Key': key},
                                                ExpiresIn=3600)
                                              
        return {
            "status": 200,
            "data": response,
            "message": "This is a presigned url to download the image"
            }
    except ClientError:
        return{
            "status":404,
            "data":"Not Found In S3 Bucket"}
    
    
#presigned url to put data in the s3 bucket    
def presigned_url_post(event, context):
    # print(event)
    client_method="put_object"
    body=json.loads(event['body'])
    key = body['image_name']



    # bucket_name="image-recognition-assessment"
    params={'Bucket': os.environ["BUCKET_NAME"], 'Key': key}
    response = s3_client.generate_presigned_url(client_method,params,
                                                     ExpiresIn=3600)
    # with open(key, 'r') as object_file:
        # object_text = object_file.read()
    # response = requests.put(response, data=object_text)

    return {
            "status": 200,
            "data": response,
            "message": "This is a presigned url to upload your image"
            }
