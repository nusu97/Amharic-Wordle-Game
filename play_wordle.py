from wordle import Wordle
from letter_state import LetterState
from colorama import Fore, init
from typing import List
from unittest.mock import DEFAULT
import random

init(autoreset=True)  

def main():
    word_set = load_word_set("wordle_words.txt")
    secret = random.choice(list(word_set))
    print("Welcome to Wordle!\n")
    wordle = Wordle(secret)  
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
        lines.append(convert_result_to_color(result))

    # Print remaining empty rows
    remaining = wordle.MAX_ATTEMPTS - len(wordle.attempts)
    for _ in range(remaining):
        lines.append("_" * wordle.WORD_LENGTH)

    draw_border_around(lines)


def load_word_set(oath: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
           word = line.strip().upper()
           word_set.add(word)
    return word_set


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
    content_width = max(len(line) for line in lines)
    content_width = max(content_width, size)

    # Top and bottom borders
    top_border = "┌" + "─" * (content_width + pad * 2) + "┐"
    bottom_border = "└" + "─" * (content_width + pad * 2) + "┘"

    print(top_border)
    for line in lines:
        # Center the line inside content width
        line_centered = line.center(content_width)
        space = " " * pad
        print(f"│{space}{line_centered}{space}│")
    print(bottom_border)


if __name__ == "__main__":
    main()
