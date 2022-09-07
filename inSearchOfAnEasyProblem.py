n = int(input())
responses = list(map(int, input().split()))
print("easy" if sum(responses) == 0 else "hard")
