t = int(input())


def find_min_moves(a, b):
    if a == b:
        return 0
    else:
        difference = abs(a - b)
        if difference % 10 == 0:
            return int(difference / 10)
        else:
            return (difference // 10) + 1


for i in range(t):
    a, b = map(int, input().split())
    min_moves = find_min_moves(a, b)
    print(min_moves)
