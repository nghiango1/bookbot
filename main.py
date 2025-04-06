from stats import count_book_characters, get_book_text


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(count_book_characters(file_contents))


main()
