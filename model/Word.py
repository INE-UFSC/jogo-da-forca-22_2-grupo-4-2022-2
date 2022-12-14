
# Fazendo deste modo a classe WORD, fica fácil alterar o objeto que gera a palvara (pouco acoplamento)
# Assim, basta apenas enviar como parametro do construtor ou mesmo setar a partir do método set_password()

class Word:
    
    def __init__(self, password="PALAVRA"):
        self.password = password
        self.mask = [False for _ in self.password]
    
    def reset(self, new_password=None):
        if not new_password is None:
            self.set_password(new_password)
        self.reset_mask()

    def reset_mask(self):
        self.mask = [False for _ in self.password]

    def get_password(self):
        return self.password

    def get_mask(self):
        return self.mask[:]
    
    def get_password_with_mask(self):
        password_with_mask = ""
        for index, letter in enumerate(self.get_password()):
            if self.mask[index]:
                password_with_mask += letter
            else:
                password_with_mask += "_"
            password_with_mask += " "
        return password_with_mask

    def get_unrevealed_letters(self):
        password = self.get_password()
        mask = self.get_mask()
        letters = []
        for index, letter in enumerate(password):
            if mask[index] == 0 and not letter in letters:
                letters.append(letter)
        return letters[:]
    
    def set_password(self, new_value):
        self.password = new_value
    
    def have(self, letter):
        return (letter in self.get_password())
    
    def reveal(self, letter):
        for index, word_letter in enumerate(self.get_password()):
            if word_letter == letter:
                self.mask[index] = True

    def is_there_letter_reveal(self):
        return (True in self.get_mask())
                
    def was_revealed(self):
        return (not False in self.get_mask())