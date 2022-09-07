import math
t = int(input())


def get_min_area(a, b):
    min_l, max_l = min(a, b), max(a, b)
    if min_l * 2 > max_l:
        return (min_l * 2) ** 2
    else:
        return max_l ** 2


for i in range(t):
    a, b = map(int, input().split())
    min_area = get_min_area(a, b)
    print(min_area)
