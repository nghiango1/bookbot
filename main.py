import sys

from stats import (
    chars_dict_to_sorted_list,
    get_book_text,
    get_chars_dict,
    get_number_of_words,
)


def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for info in sorted_list:
        if not info["character"].isalpha():
            continue
        print(f'{info["character"]}: {info["count"]}')
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, sorted_list)


main()
