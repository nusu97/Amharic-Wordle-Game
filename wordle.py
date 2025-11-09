from letter_state import LetterState
class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 4
    
    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        # store results for each attempt to avoid recomputation
        self.results = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)
        self.results.append(self.guess(word))

    def attempt_with_result(self, word: str):
        """Attempt a word and return the list of LetterState objects.
        Raises ValueError if length mismatch or attempts exhausted."""
        word = word.strip().upper()
        if len(word) != self.WORD_LENGTH:
            raise ValueError(f"Word length must be {self.WORD_LENGTH} characters")
        if not self.can_attempt:
            raise ValueError("No remaining attempts or puzzle already solved")
        self.attempt(word)
        return self.results[-1]

    def guess(self, word: str):
        word = word.upper()
        result = []
        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)

        return result
    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return  self.remaining_attempts > 0 and not self.is_solved

    def serialize_result(self, result):
        """Serialize a list[LetterState] to dictionaries for JSON."""
        return [
            {
                "char": l.character,
                "inWord": l.is_in_word,
                "inPosition": l.is_in_position
            } for l in result
        ]

    def serialize_state(self):
        """Serialize full game state for API responses."""
        return {
            "wordLength": self.WORD_LENGTH,
            "maxAttempts": self.MAX_ATTEMPTS,
            "attempts": [a for a in self.attempts],
            "results": [self.serialize_result(r) for r in self.results],
            "remainingAttempts": self.remaining_attempts,
            "solved": self.is_solved
        }
        
