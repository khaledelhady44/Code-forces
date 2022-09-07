guest = list(input())
host = list(input())
pile = list(input())

required = []
required.extend(guest)
required.extend(host)

required.sort()
pile.sort()

print("YES" if required == pile else "NO")
