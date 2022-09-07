t = int(input())

not_three = [i for i in range(0, 1667) if (i % 3 != 0 and i % 10 != 3)]


for i in range(t):
    index = int(input())
    print(not_three[index - 1])
