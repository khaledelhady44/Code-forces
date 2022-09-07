n = int(input())
poles = [input() for i in range(n)]

i = poles[0]
groups = 1
for pole in poles:
    if i != pole:
        groups += 1
        i = pole

print(groups)
