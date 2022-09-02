
import os
from Word import Word
from Player import Player
from State import InMenu
from WordGenerator import WordGenerator
from Checker import Checker
from Helper import Helper
from HelpController import HelpController
from AttemptController import AttemptController


class Game:

    def __init__(self):
        self.running = True
        
        self.word_generator = WordGenerator()
        self.word = Word(self.word_generator.get_word())
        self.player = Player()
        self.checker = Checker(self.player, self.word)
        self.helper = Helper(self.word)

        self.help_controller = HelpController(self.helper)
        self.attempt_controller = AttemptController(self.player, self.word, self.checker)

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
