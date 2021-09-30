This project is a simple Api for the recognition of images using AWS Rekognition on the back-end
The API stores an image, does image recognition on it and returns results to the user in two ways, with a callback and a GET endpoint

project workflow:
- deploy the services using sls deploy 
- you can upload an image using presigned url post request /image 
but you must specify in the request body the name of the image as json
{
    "image_name":"example.jpg"
}

- you can get an image that is already in a s3 bucket using presigned url get request /image
also you must specify in the request body the name of the image you want to get from s3 bucket as json
{
    "image_name":"example.jpg"
}

- you can get the labels of the image recognition using image unique if in /label/{id}

