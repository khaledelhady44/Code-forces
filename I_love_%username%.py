n = int(input())
contests = [int(x) for x in input().split()]

max = contests[0]
min = contests[0]
amazing_count = 0

for contest in contests:
    if contest > max:
        amazing_count += 1
        max = contest
    elif contest < min:
        amazing_count += 1
        min = contest

print(amazing_count)
