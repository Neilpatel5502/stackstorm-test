from st2common.runners.base_action import Action

__all__ = [
    'AWSBaseAction'
]

class AWSBaseAction(Action):
    def __init__(self, config):
        super(AWSBaseAction, self).__init__(config=config)
        temp_config = self._get_config()
        self.aws_region_name = temp_config["aws_region_name"]
        self.aws_access_key_id = temp_config["aws_access_key_id"]
        self.aws_secret_access_key = temp_config["aws_secret_access_key"]

    def _get_config(self):
        aws_region_name = self.config['aws_region_name']
        aws_access_key_id = self.config['aws_access_key_id']
        aws_secret_access_key = self.config['aws_secret_access_key']

        temp_config = {
            "aws_region_name": aws_region_name,
            "aws_access_key_id": aws_access_key_id,
            "aws_secret_access_key": aws_secret_access_key
        }
        return temp_config