def gridTraveler(m, n, memo={}):

    key = f"{m}, {n}"

    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    else:
        memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[key]


print(gridTraveler(18, 18))
