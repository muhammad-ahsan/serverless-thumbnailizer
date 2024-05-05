from diagrams import Diagram, Cluster, Edge

from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import SimpleStorageServiceS3Bucket

with (Diagram("Serverless Thumbnailizer", show=False, direction="LR")):
    with Cluster("AWS Cloud"):
        APIGateway("API Gateway") >> Edge(label="image upload") >> SimpleStorageServiceS3Bucket(
            "S3") >> Edge(label="UploadEvent") >> Lambda("Lambda") >> Edge(
            label="thumbnail") >> SimpleStorageServiceS3Bucket(
            "S3")
