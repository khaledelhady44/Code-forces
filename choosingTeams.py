n, k = map(int, input().split())
y = [int(x) for x in input().split()]
valid = [x for x in y if k + x <= 5]
print(len(valid) // 3)
