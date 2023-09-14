from st2common.runners.base_action import Action

class MypythonAction(Action):
    def run(self, args):
        print(args)

        return args