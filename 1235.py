__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"

# link: https://leetcode.com/problems/maximum-profit-in-job-scheduling

from functools import cache
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        data = sorted(zip(startTime, endTime, profit))

        @cache
        def _solve(t, i):
            if i >= len(startTime):
                return 0
            if t < data[i][0]:
                return _solve(data[i][0], i)
            if t > data[i][0]:
                return _solve(t, i + 1)

            return max(_solve(data[i][1], i + 1) + data[i][2], _solve(t, i + 1))

        return _solve(0, 0)
