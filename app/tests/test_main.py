import pytest
from app.main import dummyFunction, downloadFile
from os import getenv

@pytest.fixture
def dummyInput():
    return "random"

def test_dummyFunction(dummyInput):
    print(dummyInput)
    result = dummyFunction(dummyInput)
    assert result == "dummy"


def test_downloadFile():
    s3_bucket_name = getenv("BUCKET_NAME", None)
    result = downloadFile(s3_bucket_name)
    assert result == "file downloaded!!!!!!"