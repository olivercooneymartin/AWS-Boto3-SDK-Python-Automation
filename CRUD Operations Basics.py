# Demonstration of basic CRUD operations using the Python Boto3 SDK in AWS.

import boto3

s3 = boto3.resource("s3")
bucket_name = "dct-crud-1"
file_1 = "file_1.txt"
file_2 = "file_2.txt"

# CREATE
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": "us-west-2",
    },
)

# READ
obj = s3.Object(bucket_name, file_1)
body = obj.get()["Body"].read()
print(body)

# UPDATE
with open(file_2, "rb") as replacement_file:
    s3.Object(bucket_name, file_1).put(Body=replacement_file)

# DELETE
bucket = s3.Bucket(bucket_name)
bucket.delete()
