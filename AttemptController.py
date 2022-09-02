from Attempt import Attempt


class AttemptController:

    def __init__(self, player, word, checker):
        self.player = player
        self.word = word
        self.checker = checker

    def game_is_over(self):
        return self.checker.game_is_over()

    def get_result(self):
        return self.checker.get_result()

    def get_letter(self):
        letter = input("Letra: ").upper().strip()
        while (len(letter) > 1) or (not letter.isalpha()) or (letter in self.player.get_all_letters()):
            print("Escolha inválida")
            letter = input("Letra: ").upper().strip()
        return letter

    def update(self):   
        letter = self.get_letter()
        attempt = Attempt(letter)
        if self.word.have(letter):
            self.word.reveal(letter)
            attempt.set_correct(True)
        self.player.add_attempt(attempt)
        self.checker.check()
