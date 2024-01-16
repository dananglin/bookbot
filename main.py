def main():
    path = "books/frankenstein.txt"
    with open(path) as file:
        file_contents = file.read()
        report(
            path,
            get_num_words(file_contents),
            character_dict(file_contents)
        )


def get_num_words(text):
    '''get_num_words returns the number of words in a given text string'''
    words = text.split()
    return len(words)


def character_dict(text):
    '''character_dict returns a dictionary with the amount of times
    a character appears in a given text'''
    output = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for character in text:
        if character.lower() in output:
            output[character.lower()] += 1

    return output


def report(path, total_words, characters):
    '''report prints a report about the specified book'''
    print(f"--- Begin report of {path} ---")
    print(f"{total_words} words found in the document\n")
    for key, value in characters.items():
        print(f"The character '{key}' was found {value} times")
    print("--- End report ---")


main()
