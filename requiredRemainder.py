t = int(input())


def find_remainder(x, y, n):
    if n % x > y:
        return n - (n % x) + y
    elif n % x < y:
        return n - (n % x) - (x - y)
    else:
        return n


for i in range(t):
    x, y, n = map(int, input().split())
    print(find_remainder(x, y, n))
