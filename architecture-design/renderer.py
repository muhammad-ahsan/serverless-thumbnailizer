"""
This pattern creates REST API via API Gateway, acting as an S3 proxy for write operations.
Reference: https://serverlessland.com/patterns/apigw-s3-lambda-sls-py

"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import SimpleStorageServiceS3Bucket

with (Diagram("Serverless Thumbnailizer", show=False, direction="LR")):
    with Cluster("AWS Cloud"):
        APIGateway("API Gateway") >> Edge(label="image upload") >> SimpleStorageServiceS3Bucket(
            "Amazon S3 bucket") >> Edge(label="event -> s3:ObjectCreated:*") >> Lambda("AWS Lambda") >> Edge(
            label="save thumbnail") >> SimpleStorageServiceS3Bucket(
            "S3")
