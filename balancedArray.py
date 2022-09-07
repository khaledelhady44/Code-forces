no_test_cases = int(input())
for test_case in range(no_test_cases):
    length = int(input())
    even = [2 * x for x in range(1, int(length / 2) + 1)]
    odd = [x for x in range(1, length - 2, 2)]
    missing = sum(even) - sum(odd)
    if missing % 2 == 0:
        print("NO")
    else:
        print("YES")
        odd.append(missing)
        even.extend(odd)
        answer = [str(x) for x in even]
        print(" ".join(answer))
