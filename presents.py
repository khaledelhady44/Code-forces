n = int(input())
presents = list(map(int, input().split()))

answer = ["" for i in range(n)]
for i in range(n):
    answer[presents[i] - 1] = str(i + 1)

print(" ".join(answer))
