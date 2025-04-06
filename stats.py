from collections import defaultdict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def get_book_number_of_words(file_contents):
    num_words = len(file_contents.split())
    return f"{num_words} words found in the document"


def count_book_characters(file_contents):
    counter = defaultdict(int)
    for c in file_contents:
        counter[c.lower()] += 1

    return counter
