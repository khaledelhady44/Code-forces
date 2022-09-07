stops_num = int(input())
stops = [list(map(int, input().split())) for i in range(stops_num)]

min_capacity = 0
passengers = 0

for stop in stops:
    passengers = passengers - stop[0] + stop[1]
    if passengers > min_capacity:
        min_capacity = passengers

print(min_capacity)
