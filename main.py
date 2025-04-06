from stats import (
    count_book_characters,
    get_book_text,
    sort_characters_count,
    get_book_number_of_words,
)


def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    count_words = get_book_number_of_words(file_contents)
    counter = count_book_characters(file_contents)
    sorted_counter = sort_characters_count(counter)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    for info in sorted_counter:
        if not info["character"].isalpha():
            continue
        print(f'{info["character"]}: {info["count"]}')
    print("============= END ===============")


main()
