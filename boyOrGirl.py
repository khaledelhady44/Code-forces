from distutils import dist


name = input()
distinct_chars = set(name)
if len(distinct_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
