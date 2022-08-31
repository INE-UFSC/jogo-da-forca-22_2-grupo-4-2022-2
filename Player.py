
class Player:

    def __init__(self):
        self.attempts = []

    def add_attempt(self, new_attempt):
        self.attempts.append(new_attempt)

    def get_errors(self):
        errors = 0
        for attempt in self.attempts:
            if not attempt.is_correct():
                errors += 1
        return errors
        
    def get_discovered_letters(self):
        letters = []
        for attempt in self.attempts:
            if attempt.is_correct():
                letters.append(attempt.get_letter())
        return letters[:]
        
    def get_all_letters(self):
        letters = []
        for attempt in self.attempts:
            letters.append(attempt.get_letter())
        return letters[:]
        