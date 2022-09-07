n = int(input())
rooms = [list(map(int, input().split())) for i in range(n)]

answer = 0
for room in rooms:
    if room[1] - room[0] >= 2:
        answer += 1

print(answer)
