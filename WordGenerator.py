from random import randint

class WordGenerator():
    
    all_words = [
        "ALFABETO",
        "BUROCRACIA",
        "CONSELHO",
        "DEMILITARIZADO",
        "EMPRESTADO",
        "FORMALMENTE",
        "GARIMPEIRO",
        "HEMOFILIA",
        "INDIO",
        "JOGO",
        "KONDZILLA",
        "LAUDO",
        "MOMENTO",
        "NOCAUTE",
        "OMISSO",
        "PARAQUEDAS",
        "QUARTZO",
        "RONDONIA",
        "SIMPLIFICADO",
        "TROMPETA",
        "UMBIGO",
        "VERNIZ",
        "WASHINGTON",
        "XILOFONE",
        "YOGA",
        "ZORRO"
    ]
    
    def __init__(self, dictionary = all_words):
        self.dictionary = dictionary
    
    def get_word(self):
        return self.dictionary[randint(0, len(self.dictionary) - 1)]
    
    
    