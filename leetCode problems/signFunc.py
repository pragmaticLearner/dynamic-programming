class Solution:
    def arraySign(self, nums) -> int:

        t = 1
        for i in nums:
            t *= i

        if t > 0:
            return 1
        if t < 0:
            return -1
        if t == 0:
            return 0


x = Solution.arraySign(None, [99999, 99999, 3, 5, 5, -6, -7])
print(x)
