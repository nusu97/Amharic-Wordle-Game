class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    
    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass

    @property
    def is_solved(self):
        return self.attempts[-1] == self.secret
    
    @property
    def can_attempt(self):
        return len(self.attempt) < self.MAX_ATTEMPTS and not self.is_solved
        pass