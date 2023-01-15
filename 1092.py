__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/shortest-common-supersequence/


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = {(-1, -1): 0}
        back = {}

        for idx in range(len(str1)):
            dp[idx, -1] = idx + 1
        for idx in range(len(str2)):
            dp[-1, idx] = idx + 1

        for i in range(0, len(str1)):
            for j in range(0, len(str2)):
                if str1[i] == str2[j]:
                    dp[i, j] = dp[i - 1, j - 1] + 1
                    back[i, j] = (i - 1, j - 1, str1[i])
                elif dp[i - 1, j] < dp[i, j - 1]:
                    dp[i, j] = dp[i - 1, j] + 1
                    back[i, j] = (i - 1, j, str1[i])
                else:
                    dp[i, j] = dp[i, j - 1] + 1
                    back[i, j] = (i, j - 1, str2[j])

        def _backtrack(i, j):
            if (i, j) not in back:
                return list(str1[: i + 1]) + list(str2[: j + 1])
            return _backtrack(back[i, j][0], back[i, j][1]) + [back[i, j][-1]]

        return "".join(_backtrack(len(str1) - 1, len(str2) - 1))
