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