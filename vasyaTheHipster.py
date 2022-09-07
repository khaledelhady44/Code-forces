a, b = map(int, input().split())
max_fashion = min(a, b)

print(max_fashion, (max(a, b) - max_fashion) // 2)
