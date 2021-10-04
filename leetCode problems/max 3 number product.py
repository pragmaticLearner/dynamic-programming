"""
    Given an array of length n, find the maximum product
        from 3 of the arrays numbers

"""


def maximumProduct(x, nums):
    nums.sort()
    return (nums[-1] * nums[-2] * nums[-3])\
        if (nums[-1] * nums[-2] * nums[-3]) > (
            nums[-1] * nums[0] * nums[1]) else (nums[-1] * nums[0] * nums[1])


print(maximumProduct(3, [-100, -98, -1, 2, 3, 4]))
