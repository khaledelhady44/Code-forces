from re import I


n, k = map(int, input().split())
max_time = 4 * 60 - k

time_used = 0
i = 0
while(i < n):
    time_used += 5 * (i + 1)
    if time_used > max_time:
        break
    else:
        i += 1

print(i)
