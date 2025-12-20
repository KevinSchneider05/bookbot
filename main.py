# Main.py

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

#Accepts text of book as string and returns word count
def get_word_count(book_text):
    return len(book_text.split())



main()

