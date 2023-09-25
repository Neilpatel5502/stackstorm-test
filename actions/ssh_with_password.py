import paramiko
from st2common.runners.base_action import Action

class SSHWithPasswordAction(Action):
    def run(self, ec2_instance_ip, username, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            ssh.connect(ec2_instance_ip, username=username, password=password)
            
            command = "ls -l"
            stdin, stdout, stderr = ssh.exec_command(command)

            output = stdout.read().decode('utf-8')
            return (True, output)
        except Exception as e:
            return (False, str(e))
        finally:
            ssh.close()
