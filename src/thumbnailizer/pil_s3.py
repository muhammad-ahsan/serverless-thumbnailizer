# Modified with thanks from
# https://gist.github.com/ghandic/a48f450f3c011f44d42eea16a0c7014d

import os
from io import BytesIO

import boto3
from PIL import Image


class S3ImagesInvalidExtension(Exception):
    pass


class S3ImagesUploadFailed(Exception):
    pass


class S3Image(object):
    """Usage:

        images = S3Images(aws_access_key_id='fjrn4uun-my-access-key-589gnmrn90',
                          aws_secret_access_key='4f4nvu5tvnd-my-secret-access-key-rjfjnubu34un4tu4',
                          region_name='eu-west-1')
        im = images.from_s3('my-example-bucket-9933668', 'pythonlogo.png')
        im
        images.to_s3(im, 'my-example-bucket-9933668', 'pythonlogo2.png')
    """

    def __init__(self, region_name):
        self.s3 = boto3.client('s3', region_name=region_name)

    def from_s3(self, bucket, key) -> Image:
        file_byte_string = self.s3.get_object(Bucket=bucket, Key=key)['Body'].read()
        return Image.open(BytesIO(file_byte_string))

    def to_s3(self, img, bucket, key) -> bool:
        buffer = BytesIO()
        img.save(buffer, self.__get_safe_ext(key))
        buffer.seek(0)
        sent_data = self.s3.put_object(Bucket=bucket, Key=key, Body=buffer)
        if sent_data['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise S3ImagesUploadFailed('Failed to upload image {} to bucket {}'.format(key, bucket))

        return True

    def __get_safe_ext(self, key) -> str:
        ext = os.path.splitext(key)[-1].strip('.').upper()
        if ext in ['JPG', 'JPEG']:
            return 'JPEG'
        elif ext in ['PNG']:
            return 'PNG'
        else:
            raise S3ImagesInvalidExtension('Extension is invalid')
