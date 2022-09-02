from random import randint

class Helper:

    def __init__(self, word):
        self.word = word
        self.helped = False

    def reset(self):
        self.helped = False

    def set_word(self, new_word):
        self.word = new_word

    def already_helped(self):
        return self.helped

    def is_possible_to_help(self):
        return (not self.word.is_there_letter_reveal() and not self.already_helped())

    def help(self):
        letters = self.word.get_unrevealed_letters()
        self.word.reveal(letters[randint(0, len(letters) - 1)])
        self.helped = True

