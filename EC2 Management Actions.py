# This file demonstrates basic EC2 instance management actions using Boto3.

import boto3

# Create an EC2 resource and set the instance name used in this demo.
ec2 = boto3.resource("ec2")
instance_name = "dct-ec2-hol"

# Store the instance ID after finding or creating the instance.
instance_id = None

# Check whether an instance with this Name tag already exists.
# If it does not exist, create a new EC2 instance.
instances = ec2.instances.all()
instance_exists = False

for instance in instances:
    for tag in instance.tags or []:
        if tag["Key"] == "Name" and tag["Value"] == instance_name:
            instance_exists = True
            instance_id = instance.id
            print(
                f"An instance named '{instance_name}' with id "
                f"'{instance_id}' already exists."
            )
            break

    if instance_exists:
        break

if not instance_exists:
    # If the instance has not already been created, launch a new EC2 instance.
    new_instance = ec2.create_instances(
        ImageId="LINUX-AMI",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="DCT-1",
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": instance_name,
                    },
                ],
            },
        ],
    )
    instance_id = new_instance[0].id
    print(f"An instance named '{instance_name}' with id '{instance_id}' was created.")

# Stopping an instance.
# ec2.Instance(instance_id).stop()
# print(f"An instance named '{instance_name}-{instance_id}' has been stopped.")

# Starting an instance.
# ec2.Instance(instance_id).start()
# print(f"An instance named '{instance_name}-{instance_id}' has been started.")

# Terminating an instance.
# ec2.Instance(instance_id).terminate()
# print(f"An instance named '{instance_name}-{instance_id}' has been terminated.")
