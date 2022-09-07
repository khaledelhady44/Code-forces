n = int(input())
test_cases = []

for _ in range(n):
    test_cases.append([int(x) for x in input().split()])


for test_case in test_cases:
    x = test_case[0]
    y = test_case[1]
    print(y - (x % y) if x % y != 0 else 0)
