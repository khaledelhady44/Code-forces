n = int(input())
mishka_win = 0
chris_win = 0

for i in range(n):
    m, c = map(int, input().split())
    if m > c:
        mishka_win += 1
    elif c > m:
        chris_win += 1

if mishka_win > chris_win:
    print("Mishka")
elif mishka_win < chris_win:
    print("Chris")
else:
    print("Friendship is magic!^^")
