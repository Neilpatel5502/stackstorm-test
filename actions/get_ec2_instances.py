import boto3
from lib.actions import AWSBaseAction

__all__ = [
    'Ec2Instances'
]


class Ec2Instances(AWSBaseAction):
    def run(self):
        ec2_client = boto3.client(
            'ec2',
            region_name = self.aws_region_name,
            aws_access_key_id = self.aws_access_key_id,
            aws_secret_access_key = self.aws_secret_access_key
        )

        response = ec2_client.describe_instances()
        instances = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance)

        return instances