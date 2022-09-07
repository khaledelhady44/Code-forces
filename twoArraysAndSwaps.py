t = int(input())


def find_max_sum(a, b, k, n):
    a_sum = sum(a)
    b.sort(reverse=True)
    for i in range(k):
        a_copy = a[:]
        a_copy.sort()
        a_copy[0] = b[i]
        if sum(a_copy) > a_sum:
            a_sum = sum(a_copy)
            a = a_copy
        else:
            break
    return a_sum


for i in range(t):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    max_sum = find_max_sum(a, b, k, n)
    print(max_sum)
