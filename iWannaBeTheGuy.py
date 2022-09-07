n = int(input())
x_indices = input().split()
y_indices = input().split()

indices = []
indices.extend(x_indices[1:])
indices.extend(y_indices[1:])

indices = set(indices)
indices.difference_update({"0"})
if len(indices) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
