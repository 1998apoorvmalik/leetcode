__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"

# problem link: https://leetcode.com/problems/number-of-subarrays-having-even-product

from typing import List


class Solution:

    # DP Subproblem: dp(x) - number of subarrays (including x) having even product.
    # Recurrence: dp(x) = dp(x - 1) if num[x] % 2 else x + 1
    # Output sum of all dp subproblems

    def evenProduct(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            dp[idx] = dp[idx - 1] if num % 2 else idx + 1
        return sum(dp)
