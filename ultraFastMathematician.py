num1 = input()
num2 = input()

answer = ""
for i in range(len(num1)):
    if num1[i] == num2[i]:
        answer += "0"
    else:
        answer += "1"

print(answer)
