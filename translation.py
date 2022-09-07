from audioop import reverse


s = input()
t = input()
print("YES" if s[::-1] == t else "NO")
