word = input()
upper = 0
lower = 0
for letter in word:
    if letter.isupper():
        upper += 1
    else:
        lower += 1

print(word.upper() if upper > lower else word.lower())
