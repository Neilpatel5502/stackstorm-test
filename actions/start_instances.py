import boto3
from lib.actions import AWSBaseAction

__all__ = [
    'StartEC2Instances'
]


class StartEC2Instances(AWSBaseAction):
    def run(self, instance_ids):
        ec2_client = boto3.client(
            'ec2',
            region_name = self.aws_region_name,
            aws_access_key_id = self.aws_access_key_id,
            aws_secret_access_key = self.aws_secret_access_key
        )
        print("Hello")
        instances = instance_ids.split(",")
        print(f"Instances: {instances}")
        response = ec2_client.start_instances(InstanceIds=instances)
        
        return response