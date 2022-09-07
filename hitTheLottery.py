n = int(input())


def get_bills(n):

    if n >= 100:
        return n // 100 + get_bills(n % 100)
    elif n >= 20:
        return n // 20 + get_bills(n % 20)
    elif n >= 10:
        return n // 10 + get_bills(n % 10)
    elif n >= 5:
        return n // 5 + get_bills(n % 5)
    else:
        return n


print(get_bills(n))
