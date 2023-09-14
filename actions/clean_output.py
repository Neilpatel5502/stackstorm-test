from lib.actions import AWSBaseAction

__all__ = [
    'MyPythonAction'
]

class MyPythonAction(AWSBaseAction):
    def run(self, args):
        output = args.split("\n")
        return output