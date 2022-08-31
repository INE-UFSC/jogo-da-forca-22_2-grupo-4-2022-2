
# Talvez reestruturar a screen para nao receber nenhum parametro
class Screen:
    
    def render(self, password_with_mask, letters, errors):
        print("Palavra:", password_with_mask)
        print("Letras:", end=' ')
        for letter in letters:
            print(letter, end=' ')
        print("\nErros:", errors)

#  ____
# /   |
# |   O
# |  /|\
# |   |
# |  / \
# |_______
#
# A _ _ _ _ _
