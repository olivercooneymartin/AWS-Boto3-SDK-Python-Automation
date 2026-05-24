# This is an example of an RDS client method that creates an RDS DB cluster
# using AWS Boto3 with Aurora Serverless v1.

import boto3

rds = boto3.client("rds")

db_cluster_id = "your-db-cluster-id"
username = "your-master-username"
password = "your-master-password"
db_subnet_group = "your-db-subnet-group"

response = rds.create_db_cluster(
    Engine="aurora-mysql",
    EngineVersion="5.7.mysql_aurora.2.08.3",
    DBClusterIdentifier=db_cluster_id,
    MasterUsername=username,
    MasterUserPassword=password,
    DatabaseName="rds_hol_db",
    DBSubnetGroupName=db_subnet_group,
    EngineMode="serverless",
    EnableHttpEndpoint=True,
    ScalingConfiguration={
        "MinCapacity": 1,
        "MaxCapacity": 8,
        "AutoPause": True,
        "SecondsUntilAutoPause": 300,
    },
)

print(response)
