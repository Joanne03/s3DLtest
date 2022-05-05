import pytest
from app.main import dummyFunction, downloadFile

@pytest.fixture
def dummyInput():
    return "random"

def test_dummyFunction(dummyInput):
    print(dummyInput)
    result = dummyFunction(dummyInput)
    assert result == "dummy"

@pytest.fixture
def s3BucketName():
    return "model-tokenizer-files"

def test_downloadFile(s3BucketName):
    result = downloadFile(s3BucketName)
    assert result == "file downloaded!!!!!!"