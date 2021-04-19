def bestSum(targetSum, numbers, memo={}):

    # Base Case
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombo = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombo = bestSum(remainder, numbers)
        if remainderCombo is not None:
            Combo = remainderCombo + [num]
            if shortestCombo is None or (len(Combo) < len(shortestCombo)):
                shortestCombo = Combo

    memo[targetSum] = shortestCombo
    return shortestCombo


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(100, [1, 2, 5, 25]))
