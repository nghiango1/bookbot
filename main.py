from stats import (
    get_chars_dict,
    get_book_text,
    chars_dict_to_sorted_list,
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
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, sorted_list)


main()
