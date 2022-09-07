n = int(input())
welfare = [int(x) for x in input().split()]

max_welfare = max(welfare)
min_treasure = 0

for a in welfare:
    min_treasure += (max_welfare - a)

print(min_treasure)
