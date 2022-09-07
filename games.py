from turtle import home


n = int(input())
home_colors = []
guest_colors = []

for _ in range(n):
    team = input().split()
    home_colors.append(team[0])
    guest_colors.append(team[1])

result = 0
for color in guest_colors:
    result += home_colors.count(color)

print(result)
