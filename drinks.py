n = int(input())
percentages = list(map(int, input().split()))

answer = 0
for percentage in percentages:
    answer += (1 / n) * (percentage / 100)


print(answer * 100)
