
class Checker:

    def __init__(self, player, word):
        self.player = player
        self.word = word
        self.result = "CONTINUE"
    
    def set_player(self, new_player):
        self.player = new_player

    def set_word(self, new_word):
        self.word = new_word

    def get_result(self):
        return self.result

    def game_is_over(self):
        result = self.get_result()
        if result == "GANHOU" or result == "PERDEU":
            return True
        return False

    def check(self):
        if self.word.was_revealed():
            self.result = "GANHOU"
        elif not self.player.still_have_chance():
            self.result = "PERDEU"
        else:
            self.result = "CONTINUE"

