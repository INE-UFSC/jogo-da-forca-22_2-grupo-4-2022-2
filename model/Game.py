
import os
from model.Word import Word
from model.Player import Player
from model.State import InMenu
from model.WordGenerator import WordGenerator
from model.Helper import Helper
from controller.Checker import Checker
from controller.HelpController import HelpController
from controller.AttemptController import AttemptController


class Game:

    def __init__(self):
        self.running = True
        
        self.word_generator = WordGenerator()
        self.word = Word(self.word_generator.get_word())
        self.player = Player()
        self.helper = Helper(self.word)

        self.checker = Checker(self.player, self.word)
        self.help_controller = HelpController(self.helper)
        self.attempt_controller = AttemptController(self.player, self.word, self.checker)

        self.state = InMenu(self)

    def reset(self):
        self.word.reset(self.word_generator.get_word())
        self.player.reset()
        self.helper.reset()
        self.checker.reset()

    def close(self):
        self.running = False

    def is_running(self):
        return self.running
    
    def change_state(self, new_state):
        self.state = new_state

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self):
        self.state.render()
    
    def update(self):
        self.state.update()

    def handle_trasition(self):
        self.state.handle_trasition()

    def run(self):
        while self.is_running():
            self.render() 
            self.update()
            self.handle_trasition()
