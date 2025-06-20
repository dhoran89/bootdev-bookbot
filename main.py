from stats import get_num_words
from stats import get_char_words
from stats import sort_on
from stats import sort_this
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        #do something with f (file)
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = get_book_text(sys.argv[1])
    chars = get_char_words(file)
    word_count = get_num_words(file)
    dict = sort_this(chars)
    dict.sort(reverse=True,key=sort_on)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(f"{word_count} words found in the document")
    for item in dict:
        print(f"{item["char"]}: {item["num"]}")

main()
