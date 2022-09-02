from Attempt import Attempt
from Sprites import Gallows, Welcome, Goodbye, Victory, Defeat
from InputController import InputController


class State:

    def __init__(self, owner):
        self.owner = owner
    
    def update(self): ...

    def render(self):
        self.owner.clear_console()


class InMenu(State):

    def __init__(self, owner):
        super().__init__(owner)

    def render(self):
        super().render()
        print(Welcome)
        print("Este eh um jogo da forca")
        print("As regras sao bem simples")
        print("Digite uma letra do alfabeto...")
        print("Ate que voce nao tenha mais tentativas ou...")
        print("Ate que voce desvende a palavra")
        print()

    def update(self):
        option = input("Bora jogar [s/n]? ").upper().strip()
        while len(option) > 1 or not option in "SN":
            print("Por favor, escolha s (sim) ou n (nao)!")
            option = input("Quer jogar forca [s/n]? ").upper().strip()

        if option == 'S':
            self.owner.change_state(InGame(self.owner))
            self.owner.reset()
        elif option == 'N':
            self.owner.change_state(InCredits(self.owner))


class InGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def render(self):
        super().render()
        print(Gallows[self.owner.player.get_errors()])
        print(self.owner.word.get_password_with_mask())
        print("\nLetras já tentadas: ", end='')
        for letter in self.owner.player.get_all_letters():
            print(letter, end=' ')
        print()

    def update(self):
        user_input = InputController().get_input()

        if user_input == "DICA":
            self.owner.help_controller.update()
        else:
            self.owner.attempt_controller.update(user_input)
            if self.owner.attempt_controller.game_is_over():
                self.owner.change_state(InEndGame(self.owner))


class InEndGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def render(self):
        super().render()
        print(Victory if self.owner.attempt_controller.get_result() == "GANHOU"  else Defeat)

        print("A palvra secreta era " + self.owner.word.get_password())
        print()

    def update(self):
        input("Aperte enter para continuar...")
        self.owner.change_state(InMenu(self.owner))

class InCredits(State):

    def __init__(self, owner):
        super().__init__(owner)

    def render(self):
        super().render()
        print(Goodbye)
        print("\nBy Grupo 4 - Augusto, Gian, Micael, Joao\n")

    def update(self):
        input("Aperte enter para encerrar...")
        self.owner.close()
