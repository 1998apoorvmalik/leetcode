__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/maximal-square/

import collections
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = 0
        dp = collections.defaultdict(int)

        for row in range(len(matrix)):
            dp[row, 0] = 1 if matrix[row][0] == "1" else 0
            area = max(area, dp[row, 0])

        for col in range(len(matrix[0])):
            dp[0, col] = 1 if matrix[0][col] == "1" else 0
            area = max(area, dp[0, col])

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == "1":
                    dp[row, col] = 1 + min(dp[row - 1, col], dp[row, col - 1], dp[row - 1, col - 1])
                area = max(dp[row, col], area)

        return area**2
