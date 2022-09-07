no_cases = int(input())


def is_possible(test_case):
    if len(test_case) == 1:
        return True
    else:
        if test_case[1] - test_case[0] == 1 or test_case[1] == test_case[0]:
            return is_possible(test_case[1:])
        else:
            return False


for _ in range(no_cases):
    no_digits = int(input())
    test_case = [int(x) for x in input().split()]
    test_case.sort()
    print("YES" if is_possible(test_case) else "NO")
