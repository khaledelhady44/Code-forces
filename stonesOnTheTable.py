num = int(input())
stones = input()

result = 0
for i in range(num - 1):
    if stones[i] == stones[i+1]:
        result += 1

print(result)
