# My first learnt DP algorithm

# Using recursion


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(4))


# Fibonacci using DP method
def fib(n):
    if n <= 1:
        return n

    table = [None] * (n + 1)
    table[0], table[1] = 0, 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


print(fib(5))
