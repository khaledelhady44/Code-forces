year = int(input())

i = year
while True:
    i += 1
    st = str(i)
    if len(set(str(st))) == len(str(st)):
        break

print(i)
