"""
TODO

-> Fazer o banco de dados (gerenciador de palavras)
-> Arrumar tela de derrota e vitoria
-> Fazer a arte da forca (pique surrealismo neocontemporaneo)

"""

import os

class User:

    def __init__(self):
        self.chances = 5
        self.attempts = 0
        self.errors = 0
        self.word = "PALAVRA"
        self.discovered_letters = []
    
    def lost(self):
        return self.errors >= self.chances 

    def won(self):
        return (len(self.discovered_letters) == len(self.word))

    def get_errors(self):
        return self.errors

    def get_discovered_letters(self):
        return self.discovered_letters[:]

    def get_word(self):
        return self.word

    def update(self):
        letter = input("Letra: ").upper()
        # verificacao de validade da letra
        if letter in self.word:
            for index, l in enumerate(self.word):
                if l == letter:
                    self.discovered_letters.append(index)
        else:
            self.errors += 1

        self.attempts += 1


class Screen:

    def __init__(self):
        ...

    def render(self, errors, word, discovered_letters):
        # Mostrar forca
        for index, letter in enumerate(word):
            if index in discovered_letters:
                print(letter + " ", end='')
            else:
                print("_ ", end='')
        print("Erros:", errors)


class Game:

    def __init__(self):
        self.running = True
        self.user = User()
        self.screen = Screen()
        

    def close(self):
        self.running = False

    def is_running(self):
        return self.running

    def handle_update(self):
        self.user.update()
        # Arrumar isso aqui
        if self.user.lost():
            print("Perdeu")
            self.close()
        elif self.user.won():
            print("ganhou")
            self.close()

    def handle_rendering(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.screen.render(self.user.get_errors(), self.user.get_word(), self.user.get_discovered_letters())

    def game_loop(self):
        while self.is_running():
            self.handle_update()    # Lidar com a logica do jogo
            self.handle_rendering() # Renderizar o jogo

    def run(self):
        self.game_loop()


Game().run()

#  ____
# /   |
# |   O
# |  /|\
# |   |
# |  / \
# |_______
#
# A _ _ _ _ _