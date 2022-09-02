
class HelpController:

    def __init__(self, helper):
        self.helper = helper

    def already_helped(self):
        return self.helper.already_helped()

    def update(self):
        self.helper.help()
