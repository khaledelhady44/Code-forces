t = int(input())


def sus(n, tasks):
    letters = []
    prev_letter = ""
    for letter in tasks:
        if letter != prev_letter:
            if letter in letters:
                return "NO"
            else:
                letters.append(letter)
        prev_letter = letter
    return "YES"


for i in range(t):
    n = int(input())
    tasks = input()
    is_sus = sus(n, tasks)
    print(is_sus)
