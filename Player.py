
class Player:

    max_errors = 6

    def __init__(self):
        self.attempts = []

    def reset(self):
        self.attempts.clear()

    def add_attempt(self, new_attempt):
        self.attempts.append(new_attempt)

    def get_attempts(self):
        return self.attempts[:]

    def get_errors(self):
        errors = 0
        for attempt in self.get_attempts():
            if not attempt.is_correct():
                errors += 1
        return errors
        
    def get_discovered_letters(self):
        letters = []
        for attempt in self.get_attempts():
            if attempt.is_correct():
                letters.append(attempt.get_letter())
        return letters[:]
        
    def get_all_letters(self):
        letters = []
        for attempt in self.get_attempts():
            letters.append(attempt.get_letter())
        return letters[:]

    def still_have_chance(self):
        return (self.get_errors() < Player.max_errors)
        