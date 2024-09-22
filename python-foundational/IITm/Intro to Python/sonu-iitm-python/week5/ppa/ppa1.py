n = int(input())


def factorial(n):
    if n < 0:
        return -1
    if (n == 0) or (n == 1):
        return 1
    if n > 0:
        n_ki_choti_value = n-1
        return n*factorial(n_ki_choti_value)


print(factorial(n))
