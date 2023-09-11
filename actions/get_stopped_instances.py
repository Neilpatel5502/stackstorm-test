import boto3
from lib.actions import AWSBaseAction

__all__ = [
    'StoppedEC2Instances'
]


class StoppedEC2Instances(AWSBaseAction):
    def run(self):
        ec2_client = boto3.client(
            'ec2',
            region_name = self.aws_region_name,
            aws_access_key_id = self.aws_access_key_id,
            aws_secret_access_key = self.aws_secret_access_key
        )

        response = ec2_client.describe_instances(
            Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': ['stopped'],
                }
            ]
        )
        instances = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance)

        ids = [item['InstanceId'] for item in instances]
        out = ",".join(ids)

        return out