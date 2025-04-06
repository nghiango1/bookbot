from collections import defaultdict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def get_number_of_words(file_contents):
    num_words = len(file_contents.split())
    return num_words


def get_chars_dict(file_contents):
    counter = defaultdict(int)
    for c in file_contents:
        counter[c.lower()] += 1

    return counter


def sort_on(dict):
    return dict["count"]


def chars_dict_to_sorted_list(counter):
    characters = []
    for c in counter:
        characters.append({"character": c, "count": counter[c]})
    characters.sort(reverse=True, key=sort_on)
    return characters
