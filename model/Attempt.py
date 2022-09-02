
class Attempt:
    
    def __init__(self, letter="", correct=False):
        self.letter = letter
        self.correct = correct
    
    def set_correct(self, new_value):
        self.correct = new_value
        
    def get_correct(self):
        return self.correct
    
    def set_letter(self, new_value):
        self.letter = new_value
    
    def get_letter(self):
        return self.letter
    
    def is_correct(self):
        return self.get_correct()