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

        output = {
            "date": date_out,
            "uname": uname_out,
            "uptime": uptime_out,
            "Load Average": load_average,
            "Process ID": process_id,
            "User/Owner": cpu_user,
            "CPU Utilization": cpu_percent,
            "Command/Application": command,
        }
        return output