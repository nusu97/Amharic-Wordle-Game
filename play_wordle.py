from wordle import Wordle
from letter_state import LetterState
from colorama import Fore, init
from typing import List

init(autoreset=True)  # Colorama auto-reset

def main():
    print("Welcome to Wordle!\n")
    wordle = Wordle("APPLE")  # secret word

    while wordle.can_attempt:
        # Display full board every turn
        display_board(wordle)

        guess = input("\nType your guess: ").strip().upper()

        if len(guess) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word length must be {wordle.WORD_LENGTH} characters long")
            continue

        wordle.attempt(guess)

        # Check if solved immediately
        if wordle.is_solved:
            display_board(wordle)
            print(Fore.GREEN + "\nCongratulations! You solved the puzzle!")
            return

    # Game over: not solved
    display_board(wordle)
    print(Fore.RED + f"\nYou failed to solve the puzzle. The word was: {wordle.secret}")

def display_board(wordle: Wordle):
    """
    Print a fixed 6-row board: previous guesses in color, remaining rows as underscores
    """
    print("\nyour results so far...\n")
    print(f"you have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []
    # Print previous guesses in order
    for word in wordle.attempts:
        result = wordle.guess(word)
        print(convert_result_to_color(result))

    # Print remaining empty rows
    remaining = wordle.MAX_ATTEMPTS - len(wordle.attempts)
    for _ in range(remaining):
        print("_" * wordle.WORD_LENGTH)

    draw_border_around(lines)

def convert_result_to_color(result: List[LetterState]) -> str:
    """
    Convert list of LetterState to colored string
    """
    colored_result = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_result.append(color + letter.character)
    return "".join(colored_result)

def draw_border_around(lines: List[str] , size: int=9, pad: int=1):
        
    content_length = size + pad *2    
    top_border = "┌" + "─" * content_length + "┐"


if __name__ == "__main__":
    main()
