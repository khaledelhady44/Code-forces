t = int(input())


def find_min_moves(arr, n):
    count = 0
    for i in range(n):
        if arr[i] % 2 != 0 and i % 2 == 0:
            flag = True
            for j in range(n):
                if arr[j] % 2 == 0 and j % 2 != 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    count += 1
                    flag = False
                    break
            if flag:
                return -1
        elif arr[i] % 2 == 0 and i % 2 != 0:
            flag = True
            for j in range(n):
                if arr[j] % 2 != 0 and j % 2 == 0:
                    arr[i], arr[j] = arr[j], arr[i]
                    count += 1
                    flag = False
                    break
            if flag:
                return -1

    return count


for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    min_moves = find_min_moves(arr, n)
    print(min_moves)
