
import os
from Word import Word
from Player import Player
from State import InMenu
from WordGenerator import WordGenerator
from Checker import Checker
from Helper import Helper
            
class Game:

    def __init__(self):
        self.running = True
        self.word_generator = WordGenerator()
        self.word = Word(self.word_generator.get_word())
        self.player = Player()
        self.checker = Checker(self.player, self.word)
        self.helper = Helper(self.word)
        self.state = InMenu(self)

    def close(self):
        self.running = False

    def is_running(self):
        return self.running

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def reset(self):
        self.word.reset(self.word_generator.get_word())
        self.player.reset()
        self.helper.reset()
        self.result = "CONTINUE"

    def get_letter(self):
        letter = input("Letra: ").upper().strip()
        while (len(letter) > 1) or (not letter.isalpha()) or (letter in self.player.get_all_letters()):
            print("Escolha inválida")
            letter = input("Letra: ").upper().strip()
        return letter

    def is_over(self):
        return self.checker.game_is_over()

    def check(self):
        return self.checker.check()

    def get_result(self):
        return self.checker.get_result()

    def change_state(self, new_state):
        self.state = new_state

    def update(self):
        self.state.update()

    def render(self):
        self.state.render()

    def game_loop(self):
        while self.is_running():
            self.render() 
            self.update()

    def run(self):
        self.game_loop()
