__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"

# link: https://leetcode.com/problems/longest-square-streak-in-an-array

from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        dp = [1] * len(nums)
        mp = {}

        for idx in range(len(nums)):
            mp[float(nums[idx])] = idx
            target = nums[idx] ** 0.5
            if target in mp:
                dp[idx] = dp[mp[target]] + 1

        ans = max(dp)
        return ans if ans > 1 else -1
