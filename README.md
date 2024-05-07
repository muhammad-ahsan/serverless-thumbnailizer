# Serverless Thumbnailizer 

Thumbnailizer is a serverless application, designed to automate the creation of thumbnails for images uploaded to an AWS
S3 storage bucket. This application utilizes AWS services such as API Gateway, AWS Lambda, and S3 storage.

This architectural pattern creates REST API via API Gateway, acting as an S3 proxy for write operations. When an image
is uploaded to the S3 bucket, the application automatically triggers a Lambda function through API Gateway. The Lambda
function then retrieves the uploaded image from the S3 bucket and generates a thumbnail version of it. This thumbnail is
subsequently stored back into the S3 bucket, enabling easy access to both the original image and its corresponding
thumbnail.

![Architecture](https://raw.githubusercontent.com/muhammad-ahsan/serverless-thumbnailizer/ed496ca8e1f2194028dcfbf9b22ae8ced295239c/architecture-design/serverless_thumbnailizer.png)

## Local Execution

### Build

```
cd tf-resource
sam build --hook-name terraform
```

### Invoke
```
sam local invoke --hook-name terraform --event events/event.json
```

## Deployment of Infrastructure

```
terraform plan 
terraform apply
```

## Deletion of Infrastructure

```
terraform destroy
```

## Dev Dependencies

### Graphviz 
Ensure graphviz executables are on your system's PATH