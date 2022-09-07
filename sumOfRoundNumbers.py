from cgi import test


no_cases = int(input())
for _ in range(no_cases):
    test_case = input()
    no_digits = len(test_case)
    counter = 0
    rounds = []

    i = no_digits - 1
    for digit in test_case:
        if digit != "0":
            counter += 1
            rounds.append(digit + "0" * i)
        i -= 1

    print(counter)
    print(" ".join(rounds))
