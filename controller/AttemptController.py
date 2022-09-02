from model.Attempt import Attempt


class AttemptController:

    def __init__(self, player, word, checker):
        self.player = player
        self.word = word
        self.checker = checker

    def game_is_over(self):
        return self.checker.game_is_over()

    def get_result(self):
        return self.checker.get_result()

    def update(self, letter):   
        
        if letter in self.player.get_all_letters():
            return
        
        attempt = Attempt(letter)
        if self.word.have(letter):
            self.word.reveal(letter)
            attempt.set_correct(True)
        self.player.add_attempt(attempt)
