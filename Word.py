
# Fazendo deste modo a classe WORD, fica fácil alterar o objeto que gera a palvara (pouco acoplamento)
# Assim, basta apenas enviar como parametro do construtor ou mesmo setar a partir do método set_password()

class Word:
    
    def __init__(self, password="PALAVRA"):
        self.password = password
        self.mask = [False for _ in self.password]
    
    def reset(self):
        self.mask = [False for _ in self.password]

    def get_password(self):
        return self.password
    
    def get_password_with_mask(self):
        password_with_mask = ""
        for index, letter in enumerate(self.password):
            if self.mask[index]:
                password_with_mask += letter
            else:
                password_with_mask += "_"
            password_with_mask += " "
        return password_with_mask
    
    def set_password(self, new_value):
        self.password = new_value
        
    def reset_mask(self):
        self.mask = [False for _ in self.password]
    
    def have(self, letter):
        return (letter in self.password)
    
    def unravel(self, letter):
        for index, word_letter in enumerate(self.password):
            if word_letter == letter:
                self.mask[index] = True
                
    def was_unraveled(self):
        return (not 0 in self.mask)