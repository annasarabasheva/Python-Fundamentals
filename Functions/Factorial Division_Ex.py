import math

first = int(input())
second = int(input())


def fact(n, m):
    factorial_n = math.factorial(n)
    factorial_m = math.factorial(m)
    return factorial_n / factorial_m


print(f"{(fact(first, second)):.2f}")