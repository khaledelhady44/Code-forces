input_set = input()


def get_distinct_letters(letters_set):

    letters = letters_set[1: len(letters_set) - 1].split(", ")
    if len(letters) == 1 and letters[0] == "":
        return 0
    else:
        return len(set(letters))


print(get_distinct_letters(input_set))
