
class HelpController:

    def __init__(self, helper):
        self.helper = helper

    def already_helped(self):
        return self.helper.already_helped()

    def is_possible_to_help(self):
        return self.helper.is_possible_to_help()

    def update(self):
        self.helper.help()
