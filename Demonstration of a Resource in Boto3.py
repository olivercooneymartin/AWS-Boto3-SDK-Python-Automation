# Demonstration of a resource in Boto3.

import boto3

instance_id = "your-instance-id"
ec2 = boto3.resource("ec2")
instance = ec2.Instance(instance_id)

instance.start()
