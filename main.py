from stats import count_words
from stats import character_usage
from stats import dict_to_sorted_list
import sys


def get_book_text(path):
    with open(path, "r") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    characters_count = character_usage(book_text)
    sorted_characters = dict_to_sorted_list(characters_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path)
    print("----------- Word Count ----------")
    print("Found " + str(word_count) + " total words")
    print("--------- Character Count -------")
    for character, count in sorted_characters:
        print(f"{character}: {count}")

main()
