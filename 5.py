__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/longest-palindromic-substring

# flake8: noqa: E471
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.sol2(s)

    # approach 1: expand around center | TC: O(n^2) | SC: O(1)
    def sol1(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            l, r = i - 1, i + 1
            while l > -1 and s[l] == s[i]:
                l -= 1
            while r < len(s) and s[i] == s[r]:
                r += 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(longest):
                longest = s[l + 1 : r]
        return longest

    # approach 2: dynamic programming | TC: O(n^2) | SC: O(n^2)
    def sol2(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        pair = (0, 0)

        for i in range(1, len(s)):
            dp[i][i] = True
            if s[i - 1] == s[i]:
                dp[i - 1][i] = True
                pair = (i - 1, i)

        for span in range(3, len(s) + 1):
            for l in range(0, len(s) - span + 1):
                r = l + span - 1
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    if r - l > pair[1] - pair[0]:
                        pair = (l, r)

        return s[pair[0] : pair[1] + 1]
