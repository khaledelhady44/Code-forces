no_events = int(input())
events = [int(x) for x in input().split()]

officers = 0
untreated_crimes = 0

for event in events:
    if event < 0:
        if officers == 0:
            untreated_crimes += 1
        else:
            officers -= 1
    else:
        officers += event

print(untreated_crimes)
