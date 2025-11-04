from wordle import Wordle
from colorama import Fore

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
        print(*result, sep="\n")

    if wordle.is_solved:
        print("you have solved the puzzle.")
    else:
        print("you failed to sdolve the puzzle!")

def display_results(wordle: Wordle):
    for word in wordle.attempts:
        result = wordle.guess(word)
    pass

if __name__ == "__main__":
    main()