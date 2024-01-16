from aws_cdk import (
    Stack,
)

import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_secretsmanager as secretsmanager
import aws_cdk.aws_rds as rds

from constructs import Construct

class RdsBugStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc.from_lookup(
            scope=self, id="VPC",
            is_default=True
        )

        db_secret = secretsmanager.Secret.from_secret_name_v2(
            self, "DBUserSecret", secret_name="db-secret"
        )

        rds.DatabaseInstance(
            self,
            "DBInstance",
            instance_identifier="my-db",
            database_name="mydatabase",
            engine=rds.DatabaseInstanceEngine.POSTGRES,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T4G, ec2.InstanceSize.MICRO
            ),
            credentials=rds.Credentials.from_secret(secret=db_secret),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )
