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
        # Adicionar o gerador de palavras e enviar como parametro no construtor de Word
        self.word = Word()
        self.player = Player()
        self.screen = Screen()

    def close(self):
        self.running = False

    def is_running(self):
        return self.running

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_input(self):
        letter = input("Letra: ").upper().strip()
        while not (len(letter) == 1 and letter.isalpha()):
            print("Tente novamente, mas agora inserindo apenas uma letra!")
            letter = input("Letra: ").upper().strip()
        return letter

    def update(self):
        letter = self.get_input()
        attempt = Attempt(letter)
        if self.word.have(letter):
            self.word.unravel(letter)
            attempt.set_correct(True)
        self.player.add_attempt(attempt)
        
    def check_result(self):
        if self.word.was_unraveled():
            # Alterar para tela de vitoria ao inves de fechar o programa
            self.close()
        elif not self.player.still_have_chance():
            # Alterar para tela de derrota ao inves de fechar o programa
            self.close()

    def render(self):
        self.clear_console()
        self.screen.render(self.word.get_password_with_mask(), self.player.get_all_letters(), self.player.get_errors())

    def game_loop(self):
        while self.is_running():
            self.update()
            self.check_result()
            self.render() 

    def run(self):
        # Mostrar a apresentacao, onde ficará uma breve explicação do jogo. Por exemplo, self.show_presentation()
        self.game_loop()
        # Mostrar creditos, onde estará o grupo e a data de criação. Por exemplo, self.show_credits()
