from wordle import Wordle

def main():
    print("Hello World") 
    wordle = Wordle("APPLE")
    print(wordle)

    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempts(x)
    if wordle.is_solved:
        print("you have solved the puzzle.")

if __name__ == "__main__":
    main()