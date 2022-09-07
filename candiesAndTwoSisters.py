def find_ways(n):
    min_a = n / 2 + 0.5 if n % 2 != 0 else n / 2 + 1
    return int(n - min_a)


cases_no = int(input())
for _ in range(cases_no):
    case = int(input())
    print(find_ways(case))
