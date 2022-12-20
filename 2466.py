__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"

# link: https://leetcode.com/problems/count-ways-to-build-good-strings

MOD = int(1e9 + 7)


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        dp[0] = 1

        for n in range(1, high + 1):
            dp[n] = 0
            if n - zero >= 0:
                dp[n] += dp[n - zero]
            if n - one >= 0:
                dp[n] += dp[n - one]

        total = 0
        for x in range(low, high + 1):
            total += dp[x]

        return total % MOD
