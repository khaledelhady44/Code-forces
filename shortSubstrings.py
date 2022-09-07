t = int(input())


def get_a(b):
    a = b[:2]
    for i in range(2, len(b)):
        if i % 2 != 0:
            a += b[i]
    return a


for i in range(t):
    b = input()
    print(get_a(b))
