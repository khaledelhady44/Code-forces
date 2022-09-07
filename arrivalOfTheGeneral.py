n = int(input())
heights = [int(x) for x in input().split()]
steps = 0

max_height = max(heights)
max_index = heights.index(max_height)
steps += max_index

heights.remove(max_height)
heights.insert(0, max_height)

min_height = min(heights)
min_index = heights[::-1].index(min_height)
steps += min_index

print(steps)
