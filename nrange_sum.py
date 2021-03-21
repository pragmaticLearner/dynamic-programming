# Calculate sum of first n numbers


# by recursion
def _sum(n):
    if n <= 1:
        return n
    else:
        return n + _sum(n - 1)


print(_sum(5))

# by DP top down method

def Sum(n) -> int:
    cache = {}

    if n <= 1:
        return n
    else:
        cache[n] = n + Sum(n - 1)
        return cache[n]


print(Sum(5))
