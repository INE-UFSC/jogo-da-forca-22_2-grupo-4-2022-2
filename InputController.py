
class InputController:

    def verified_input(self, user_input):
        return not (user_input == "DICA" or (user_input.isalpha() and len(user_input) == 1))

    def get_input(self):
        print("\nOpcoes de entrada: \n - Dica apenas quando a palavra nao tem letra revelada \n - Pode sempre inserir uma letra qualquer\n")
        user_input = input("Tente uma letra ou peca uma dica: ").upper().strip()
        while self.verified_input(user_input):
            print("Entrada invalida")
            user_input = input("Tente uma letra ou peca uma dica: ").upper().strip()
        return user_input