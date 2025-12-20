# Main.py

import sys

from stats import get_num_words, get_num_char, sort_num_char

def main():


    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    sorted_chars = sort_num_char(get_num_char(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha() is True:
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()

