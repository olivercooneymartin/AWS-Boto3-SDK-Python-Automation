# Demonstration of a client in Boto3.

import boto3

instance_id = "your-instance-id"
client = boto3.client("ec2")
response = client.describe_instances(InstanceIds=[instance_id])

tags = response["Reservations"][0]["Instances"][0].get("Tags", [])

for tag in tags:
    print(f"{tag['Key']}: {tag['Value']}")
