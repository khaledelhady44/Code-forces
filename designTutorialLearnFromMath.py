n = int(input())


def is_prime(n):
    answer = True
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            answer = False
            break
    return answer


for i in range(n):
    if not is_prime(i):
        if not is_prime(n - i):
            print(i, n-i)
            break
