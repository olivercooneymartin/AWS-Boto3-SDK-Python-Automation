# AWS Python Boto3 CRUD demo using S3 resources.

import boto3

# Create a Boto3 S3 resource and name the bucket used in this demo.
s3 = boto3.resource("s3")
bucket_name = "dct-crud-1"

# Check whether the bucket already exists. If not, create it.
all_my_buckets = [bucket.name for bucket in s3.buckets.all()]

if bucket_name not in all_my_buckets:
    print(f"'{bucket_name}' bucket does not exist. Creating a new bucket...")
    s3.create_bucket(Bucket=bucket_name)
    print(f"'{bucket_name}' bucket has been created.")
else:
    print(f"'{bucket_name}' bucket already exists.")

# Create two local files, file_1.txt and file_2.txt, before running this script.
# In a Cloud9 terminal, you can use:
#
# $ touch file_1.txt file_2.txt
#
# Add whatever text you want to the files for the demo.
file_1 = "file_1.txt"
file_2 = "file_2.txt"

# CREATE: Upload file_1 to the S3 bucket.
s3.Bucket(bucket_name).upload_file(Filename=file_1, Key=file_1)

# READ: Read and print file_1 from the bucket.
obj = s3.Object(bucket_name, file_1)
body = obj.get()["Body"].read()
print(body)

# UPDATE: Replace the contents of file_1 with the contents of file_2.
with open(file_2, "rb") as replacement_file:
    s3.Object(bucket_name, file_1).put(Body=replacement_file)

obj = s3.Object(bucket_name, file_1)
body = obj.get()["Body"].read()
print(body)

# DELETE: Delete the object, then delete the bucket.
s3.Object(bucket_name, file_1).delete()

bucket = s3.Bucket(bucket_name)
bucket.delete()
