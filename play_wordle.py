from wordle import Wordle

def main():
    print("Hello World") 
    wordle = Wordle("APPLE")
    

    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempt(x)

    if wordle.is_solved:
        print("you have solved the puzzle.")
    else:
        print("you failed to sdolve the puzzle!")

if __name__ == "__main__":
    main()