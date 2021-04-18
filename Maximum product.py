# Leet code problem
# Solved by brute force

class Solution:
    def maxProduct(self, nums) -> int:

        i = max(nums)
        nums.remove(i)
        j = max(nums)
        return (i - 1) * (j - 1)




x = Solution.maxProduct(None, [2, 3, 4, 5])
print(x)
