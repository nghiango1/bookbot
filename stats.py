from collections import defaultdict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def get_book_number_of_words(path_to_file):
    file_contents = get_book_text(path_to_file)
    num_words = len(file_contents.split())
    return f"{num_words} words found in the document"


def count_book_characters(path_to_file):
    counter = defaultdict(int)
    for c in get_book_text(path_to_file):
        counter[c.lower()] += 1

    return counter
