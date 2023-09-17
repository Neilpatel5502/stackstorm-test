from st2common.runners.base_action import Action
import subprocess

class ExecuteCommandAction(Action):
    def run(self, command):
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                return (True, result.stdout)
            else:
                return (False, result.stderr)
        except Exception as e:
            return (False, str(e))