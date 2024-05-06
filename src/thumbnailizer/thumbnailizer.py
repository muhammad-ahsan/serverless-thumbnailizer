import urllib.parse
from typing import Any

from pil_s3 import S3Image

THUMBNAILS_STORE = "thumbnails/"


def lambda_handler(event, context):
    region = event['Records'][0]['awsRegion']
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    status, msg = save_thumbnail(region, bucket, key)
    return {
        'statusCode': status,
        'body': msg
    }


def save_thumbnail(region: str, s3_bucket: str, key: str) -> tuple[int, str]:
    s3_image: S3Image = S3Image(region_name=region)
    im: Any = s3_image.from_s3(s3_bucket, key)
    print("Successful S3 image read")
    im.thumbnail((128, 128))
    try:
        s3_image.to_s3(im, s3_bucket, _get_thumbnail_filename(key))
    except RuntimeError:
        return 500, "Unsuccessful S3 thumbnail write"

    return 200, "Successful S3 thumbnail write"


def _get_thumbnail_filename(key: str) -> str:
    tokens = key.split("/")
    return THUMBNAILS_STORE + tokens[-1]

#
# if __name__ == '__main__':
#     lambda_handler(None, None)
