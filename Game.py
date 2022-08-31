"""
TODO

-> Fazer o banco de dados (gerenciador de palavras)
-> Arrumar tela de derrota e vitoria
-> Fazer a arte da forca (pique surrealismo neocontemporaneo)

"""

import os
from Word import Word
from Player import Player
from Attempt import Attempt
from Screen import Screen
        
            
class Game:

    def __init__(self):
        self.running = True
        self.word = Word()
        self.player = Player()
        self.screen = Screen()

    def close(self):
        self.running = False

    def is_running(self):
        return self.running

    def clean_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def handle_update(self):
        letter = input("Letra: ").upper().strip()
        attempt = Attempt(letter)
        if self.word.have(letter):
            self.word.unravel(letter)
            attempt.set_correct(True)
        self.player.add_attempt(attempt)
        
    def check_result(self):
        if self.word.was_unraveled():
            self.close()

    def handle_rendering(self):
        self.clean_console()
        self.screen.render(self.word.get_password_with_mask(), self.player.get_all_letters(), self.player.get_errors())

    def game_loop(self):
        while self.is_running():
            self.handle_update()
            self.check_result()
            self.handle_rendering() 

    def run(self):
        self.game_loop()
