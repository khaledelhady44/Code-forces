n, k, l, c, d, p, nl, np = map(int, input().split())
lemon_toasts = c * d
salt_toasts = p // np
drink_toasts = (k * l) // nl

print(min(lemon_toasts, salt_toasts, drink_toasts) // n)
