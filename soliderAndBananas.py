k, n, w = map(int, input().split())
price = sum([k*x for x in range(w + 1)])
print(price - n if price - n > 0 else 0)
