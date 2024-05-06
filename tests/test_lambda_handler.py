import sys

import pytest

sys.path.append("src/thumbnailizer")  # noqa

from src.thumbnailizer.thumbnailizer import lambda_handler, get_thumbnail_filename, THUMBNAILS_STORE


@pytest.fixture()
def s3obj_created_event():
    # Sample event data for an S3 object created event
    event = {
        "Records": [
            {
                "eventVersion": "2.1",
                "eventSource": "aws:s3",
                "awsRegion": "us-east-1",
                "eventTime": "2022-05-06T12:00:00.000Z",
                "eventName": "ObjectCreated:Put",
                "userIdentity": {
                    "principalId": "AWS:XXXXXXXXXXXX:myuser"
                },
                "requestParameters": {
                    "sourceIPAddress": "192.168.1.1"
                },
                "responseElements": {
                    "x-amz-request-id": "EXAMPLE123456789",
                    "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "testConfigRule",
                    "bucket": {
                        "name": "my-bucket",
                        "ownerIdentity": {
                            "principalId": "EXAMPLE"
                        },
                        "arn": "arn:aws:s3:::my-bucket"
                    },
                    "object": {
                        "key": "example.txt",
                        "size": 1024,
                        "eTag": "0123456789abcdef0123456789abcdef",
                        "sequencer": "0A1B2C3D4E5F678901"
                    }
                }
            }
        ]
    }

    return event


@pytest.fixture
def mock_save_thumbnail(monkeypatch):
    def mocked_response(region, bucket, key):  # noqa
        return 200, "Successful S3 thumbnail write"

    monkeypatch.setattr("src.thumbnailizer.thumbnailizer.save_thumbnail", mocked_response)


def test_lambda_handler(s3obj_created_event, mock_save_thumbnail):
    response = lambda_handler(s3obj_created_event, None)
    assert response["statusCode"] == 200


@pytest.mark.parametrize("path, expected", [
    ("/path/to/image.jpg", "image.jpg"),
    ("image.jpg", "image.jpg"),
])
def test_get_thumbnail_filename(path, expected):
    with pytest.raises(ValueError) as _:
        get_thumbnail_filename(None)  # noqa
    with pytest.raises(ValueError) as _:
        get_thumbnail_filename("")  # noqa

    filename: str = get_thumbnail_filename(path)
    assert filename == THUMBNAILS_STORE + expected
