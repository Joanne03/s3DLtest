import boto3
import os

def dummyFunction(randomInput):
    print("dummyFunctionCalled")
    return "dummy"

def downloadFile(s3_bucket_name):
    s3 = boto3.resource("s3")
    tmp_path = "/tmp/"
    file = "tokenizer.json"

    s3.Bucket(s3_bucket_name).download_file(file, tmp_path + file)
    print(os.listdir(tmp_path))
    return "file downloaded!!!!!!"
