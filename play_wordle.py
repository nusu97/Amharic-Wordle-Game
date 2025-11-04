from wordle import Wordle

def main():
    print("Hello World") 
    wordle = Wordle("APPLE")
    print(wordle)

    while True:
        x = input("Type your guess: ")
        if x == wordle.secret:
            print("you have guessed the word!")
            break
        print("your guess is incorrect")
if __name__ == "__main__":
    main()