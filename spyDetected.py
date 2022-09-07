t = int(input())


def find_diff_index(arr):
    val1 = arr[0]
    val2 = arr[1]
    for i in range(2, len(arr)):
        if val1 == val2:
            if arr[i] != val1:
                return i + 1
        else:
            if arr[i] != val1:
                return 1
            else:
                return 2


for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(find_diff_index(arr))
