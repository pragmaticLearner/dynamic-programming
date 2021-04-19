"""
Add on from canSum where we return the
    list of values that add up to a specific value

"""


def howSum(targetSum, nums, memo={}):

    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in nums:
        remainder = targetSum - num
        remainderResult = howSum(remainder, nums, memo)
        if remainderResult is not None:
            memo[targetSum] = remainderResult + [num]
            return memo[targetSum]

    memo[targetSum] = None
    return None


print(howSum(300, [7, 14]))
