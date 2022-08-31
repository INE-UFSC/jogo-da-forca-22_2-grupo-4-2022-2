from Attempt import Attempt


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

    def update(self):
        option = input("Quer jogar forca [s/n]? ").upper().strip()
        while len(option) > 1 or not option in "SN":
            print("Por favor, escolha s (sim) ou n (nao)!")
            option = input("Quer jogar forca [s/n]? ").upper().strip()

        if option == 'S':
            self.owner.change_state(InGame(self.owner))
            self.owner.reset()
        elif option == 'N':
            self.owner.close()


class InGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def render(self):
        super().render()
        print(self.owner.word.get_password_with_mask())
        print(self.owner.player.get_all_letters())
        print(self.owner.player.get_errors())

    def update(self):
        letter = self.owner.get_input()
        attempt = Attempt(letter)
        if self.owner.word.have(letter):
            self.owner.word.unravel(letter)
            attempt.set_correct(True)
        self.owner.player.add_attempt(attempt)

        self.owner.result = self.owner.check_result()
        if self.owner.result == "GANHOU" or self.owner.result == "PERDEU":
            self.owner.change_state(InEndGame(self.owner))


class InEndGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def render(self):
        super().render()
        print("Fim do jogo")
        print(self.owner.word.get_password())
        print(self.owner.get_result())

    def update(self):
        input("Aperte enter para continuar")
        self.owner.change_state(InMenu(self.owner))
