__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/maximal-rectangle/

import collections
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        dp = collections.defaultdict()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col == 0:
                    dp[row, col] = (1, 1) if matrix[row][col] == "1" else (0, 0)
                else:
                    width = 1 + dp[row, col - 1][1]
                    dp[row, col] = (width, width) if matrix[row][col] == "1" else (0, 0)

                curr_min_width = dp[row, col][1]
                for k in range(row - 1, -1, -1):
                    curr_min_width = min(curr_min_width, dp[k, col][1])
                    dp[row, col] = (max(dp[row, col][0], (row - k + 1) * curr_min_width), dp[row, col][1])

                max_area = max(max_area, dp[row, col][0])

        return max_area
