def main():
    input_file_path = "amharic_words.txt"
    output_file_path = "wordle_words.txt"
    four_letter_words = []

    # Read words from input file
    with open(input_file_path, "r", encoding="utf-8") as f:  # use encoding for Amharic
        for line in f:
            word = line.strip()
            if len(word) == 4:
                four_letter_words.append(word)
    
    # Write four-letter words to output file
    with open(output_file_path, "w", encoding="utf-8") as f:
        for word in four_letter_words:
            f.write(word + "\n")  # fixed typo: 'world' -> 'word' and '/n' -> '\n'
    
    print(f"Found {len(four_letter_words)} four-letter words")

if __name__ == "__main__":
    main()
