from st2common.runners.base_action import Action

class MyEchoAction(Action):

    def run(self):
        self.logger.info("Hello world")
        return (True, "success")
