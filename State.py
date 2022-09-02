from Attempt import Attempt
from Sprites import Gallows, Welcome, Goodbye, Victory, Defeat


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
        print("ate que voce nao tenha mais tentativas ou...")
        print("ate que voce desvende a palavra")
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

        if self.owner.helper.is_possible_to_help():
            need_help = input("Deseja alguma dica [s/n]? ").upper().strip()
            while len(need_help) != 1 or not need_help in "SN":
                print("Nao entendi. Digite novamente!")
                need_help = input("Deseja alguma dica [s/n]? ").upper().strip()
            if need_help == "S" and not self.owner.helper.already_helped():
                self.owner.helper.help()
                return

        letter = self.owner.get_letter()
        attempt = Attempt(letter)
        if self.owner.word.have(letter):
            self.owner.word.reveal(letter)
            attempt.set_correct(True)
        self.owner.player.add_attempt(attempt)

        self.owner.check()
        if self.owner.is_over():
            self.owner.change_state(InEndGame(self.owner))


class InEndGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def render(self):
        super().render()
        print(Victory if self.owner.get_result() == "GANHOU"  else Defeat)

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
