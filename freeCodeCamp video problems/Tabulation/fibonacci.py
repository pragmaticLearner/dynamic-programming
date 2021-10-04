def fib(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(500))


sal_info = {"Atlanta": 120000, "Boston": 20000}
treeOrders10 = {k:v for k, v in sal_info.items() if v > 100000}

print(treeOrders10)