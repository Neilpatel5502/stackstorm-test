from st2common.runners.base_action import Action

class MypythonAction(Action):
    def run(self, *args):
        output = list(args)

        for i in output:
            print(i)

        return 1