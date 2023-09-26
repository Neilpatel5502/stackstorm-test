import paramiko
import math
from st2common.runners.base_action import Action

class SSHWithPasswordAction(Action):
    def execute_command(self, ssh, command):
        _, stdout, _ = ssh.exec_command(command)
        output = stdout.read().decode('utf-8').strip()
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
            sar_cpu_free = self.execute_command(ssh, "sar -u 5 5 | grep -E 'Average:' | awk '{print $8}'")
            sar_cpu_utilization = 100 - float(sar_cpu_free)
            sar_mem_utilization = self.execute_command(ssh, "sar -r 5 5 | grep -E 'Average:' | awk '{print $5}'")
            sar_swap_utilization = self.execute_command(ssh, "sar -S 5 5 | grep -E 'Average:' | awk '{print $4}'")
            sar_sys_data = self.execute_command(ssh, "sar -q 5 5 | grep -E 'Average:' | awk '{print $2, $3, $4, $5, $6}'")
            sar_sys_processes, sar_sys_threads, sys_load_1, sys_load_2, sys_load_3 = sar_sys_data.split(" ")
            sar_sysload_avg_min = math.ceil(min(float(sys_load_1), float(sys_load_2), float(sys_load_3)))
            sar_sysload_avg_max = math.floor(max(float(sys_load_1), float(sys_load_2), float(sys_load_3)))

            output = {
                "date": date,
                "uname": uname,
                "uptime": uptime,
                "Load Average": load_average,
                "Process ID": process_id,
                "User/Owner": cpu_user,
                "CPU Utilization": cpu_percent,
                "Command/Application": command,
                "SAR Free/Idle": f"{sar_cpu_free} (Average)",
                "SAR CPU Utilization": f"{sar_cpu_utilization} (Average)",
                "SAR MEM Utilization": f"{sar_mem_utilization} (Average)",
                "SAR SWAP Utilization": f"{sar_swap_utilization} (Average)",
                "Processes in Running/Queue": sar_sys_processes,
                "threads in Running/Queue": sar_sys_threads,
                "System Load Average is in between": f"{sar_sysload_avg_min}~{sar_sysload_avg_max}",
            }

            return (True, output)
        except Exception as e:
            return (False, str(e))
        finally:
            ssh.close()
