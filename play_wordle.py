from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
from typing import List
from colorama import init
init(autoreset=True)

def main():
    print("Hello World") 
    wordle = Wordle("APPLE")
    

    while wordle.can_attempt:
        x = input("Type your guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"word length must be {wordle.WORD_LENGTH} characters long" + Fore.RESET)
            continue

        wordle.attempt(x)
        result = wordle.guess(x)
        colored_result = convert_result_to_color(result)
        print(colored_result)

    if wordle.is_solved:
        print(Fore.GREEN + "you have solved the puzzle.")
    else:
        print(Fore.RED + "you failed to sdolve the puzzle!")

def display_results(wordle: Wordle):
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)
    pass

    for _ in range(wordle.resmaining_attempts):
        print("-" * wordle.WORD_LENGTH)
        
def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character 
        result_with_color.append(colored_letter)
    return "".join(result_with_color)

if __name__ == "__main__":
    main()