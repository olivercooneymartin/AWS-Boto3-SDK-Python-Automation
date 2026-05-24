# Launching a new EC2 instance with Boto3.

import boto3

ec2 = boto3.resource("ec2")

new_instance = ec2.create_instances(
    ImageId="ami-0889a44b331db0194",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,
    Placement={
        "AvailabilityZone": "us-east-1e",
    },
    SecurityGroupIds=[
        "sg-07686e06e0541d6b",
    ],
    KeyName="DCT-3",
    SubnetId="subnet-08a488423a06d2980",
    UserData="#!/bin/bash\necho 'Hello, World!' > /home/ec2-user/hello.txt\n",
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "My Linux Instance",
                },
            ],
        },
    ],
)

print(new_instance)
