inputs = [int(x) for x in input().split()]
inputs.sort()
a = inputs[3] - inputs[0]
b = inputs[3] - inputs[1]
c = inputs[3] - inputs[2]

print(a, b, c)
