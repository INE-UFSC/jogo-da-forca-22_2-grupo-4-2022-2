
import os
from Word import Word
from Player import Player
from State import InMenu
from FakeDictionary import FakeDictionary
            
class Game:

    def __init__(self):
        self.word_pool = FakeDictionary();
        self.running = True
        self.word = Word(self.word_pool.get_random_word())
        self.player = Player()
        self.state = InMenu(self)
        self.result = ""

    def close(self):
        self.running = False

    def is_running(self):
        return self.running

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_input(self):
        letter = input("Letra: ").upper().strip()
        while (len(letter) > 1) or (not letter.isalpha()) or (letter in self.player.get_all_letters()):
            print("Escolha inválida")
            letter = input("Letra: ").upper().strip()
        return letter

    def check_result(self):
        if self.word.was_unraveled():
            return "GANHOU"
        elif not self.player.still_have_chance():
            return "PERDEU"
        return "CONTINUE"

    def get_result(self):
        return self.result

    def change_state(self, new_state):
        self.state = new_state

    def reset(self):
        self.word.set_password(self.word_pool.get_random_word());
        self.word.reset()
        self.player.reset()
        self.result = "CONTINUE"

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
