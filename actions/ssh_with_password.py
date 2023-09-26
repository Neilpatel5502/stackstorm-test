import paramiko
from st2common.runners.base_action import Action

class SSHWithPasswordAction(Action):
    def execute_command(self, ssh, command):
        _, stdout, _ = ssh.exec_command(command)
        output = stdout.read().decode('utf-8')
        return output


    def run(self, ec2_instance_ip, username, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        try:
            ssh.connect(ec2_instance_ip, username=username, password=password)
            
            date = self.execute_command(ssh, "date")
            uname = self.execute_command(ssh, "uname -a | awk '{print $2}'")
            uptime = self.execute_command(ssh, "uptime | awk -F 'up |, | users' '{print $2}'")
            load_average = self.execute_command(ssh, "top -b -n 1 -o %CPU | grep -oP 'load average: \K.*$'")
            cpu_process_data = self.execute_command(ssh, "top -b -n 1 -o %CPU | grep -E '^\s*[0-9]+' | head -n 1 | awk '{print $1, $2, $9, $12}'")
            process_id, cpu_user, cpu_percent, command = cpu_process_data.split(" ")

            output = {
                "date": date,
                "uname": uname,
                "uptime": uptime,
                "Load Average": load_average,
                "Process ID": process_id,
                "User/Owner": cpu_user,
                "CPU Utilization": cpu_percent,
                "Command/Application": command,
            }

            return (True, output)
        except Exception as e:
            return (False, str(e))
        finally:
            ssh.close()
