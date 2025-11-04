class Wordle:
    
    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass