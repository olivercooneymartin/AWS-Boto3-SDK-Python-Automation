# Stop, start, and terminate an EC2 instance using Boto3.

import boto3

ec2 = boto3.resource("ec2")
instance_id = "your-instance-id"

# Stop an instance.
ec2.Instance(instance_id).stop()

# Start an instance.
ec2.Instance(instance_id).start()

# Terminate an instance.
ec2.Instance(instance_id).terminate()
