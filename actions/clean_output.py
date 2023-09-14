from st2common.runners.base_action import Action

class MypythonAction(Action):
    def run(self, args):
        
        with open("output.txt", "w") as file:
            file.write(f"{args}")

        return args