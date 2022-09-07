n, m = map(int, input().split())

is_right = True
for row in range(1, n + 1):
    if row % 2 != 0:
        print("#" * m)
    else:
        if is_right:
            print("." * (m - 1) + "#")
            is_right = not is_right
        else:
            print("#" + "." * (m-1))
            is_right = not is_right
