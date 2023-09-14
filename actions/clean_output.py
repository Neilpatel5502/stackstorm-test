from lib.actions import AWSBaseAction

__all__ = [
    'MyPythonAction'
]

class MyPythonAction(AWSBaseAction):
    def run(self, args):
        
        with open("/opt/stackstorm/output.txt", "w") as file:
            file.write(f"{args}")

        return args