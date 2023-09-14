import math
from lib.actions import AWSBaseAction

__all__ = [
    'MyPythonAction'
]

class MyPythonAction(AWSBaseAction):
    def run(self, args):
        output = args.split("\n")
        date_out = output[0]
        uname_out = output[1]
        uptime_out = output[2]
        load_average = output[3]
        process_id, cpu_user, cpu_percent, command = output[4].split(" ")
        sar_cpu_free = output[5]
        # sar_cpu_utilization = 100 - sar_cpu_free
        sar_mem_utilization = output[6]
        sar_swap_utilization = output[7]
        sar_sys_processes, sar_sys_threads, sys_load_1, sys_load_2, sys_load_3 = output[8].split(" ")
        sar_sysload_avg_min = math.ceil(min(float(sys_load_1), float(sys_load_2), float(sys_load_3)))
        sar_sysload_avg_max = math.floor(max(float(sys_load_1), float(sys_load_2), float(sys_load_3)))

        output = {
            "date": date_out,
            "uname": uname_out,
            "uptime": uptime_out,
            "Load Average": load_average,
            "Process ID": process_id,
            "User/Owner": cpu_user,
            "CPU Utilization": cpu_percent,
            "Command/Application": command,
            "SAR Free/Idle": f"{sar_cpu_free} (Average)",
            "SAR CPU Utilization": f"test (Average)",
            "SAR MEM Utilization": f"{sar_mem_utilization} (Average)",
            "SAR SWAP Utilization": f"{sar_swap_utilization} (Average)",
            "Processes in Running/Queue": sar_sys_processes,
            "threads in Running/Queue": sar_sys_threads,
            "System Load Average is in between": f"{sar_sysload_avg_min}~{sar_sysload_avg_max}",
        }
        return output