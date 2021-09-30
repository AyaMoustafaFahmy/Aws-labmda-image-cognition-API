This project is a simple Api for the recognition of images using AWS Rekognition on the back-end
The API stores an image, does image recognition on it and returns results to the user in two ways, with a callback and a GET endpoint

project workflow:
- deploy the services using sls deploy 
- you can upload an image first you need a presigned url from a post request /image 
but you must specify in the request body the name of the image as json

{
    "image_name":"example.jpg"
}

to upload an image using the below command

curl -X PUT -T "example_image.jpg" "presigned_url"

- you can get an image that is already in a s3 bucket using presigned url get request /image
also you must specify in the request body the name of the image you want to get from s3 bucket as json

{
    "image_name":"example.jpg"
}

- you can get the labels of the image recognition using image unique if in /label/{id}


please follow this link to find swagger api documentation for image_recognition

https://app.swaggerhub.com/apis-docs/ayamoustafa/image_recognition/0.1#/
