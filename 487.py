__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/max-consecutive-ones-ii/

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_score, current_score, restricted_score = 0, 0, 0
        for e in nums:
            if e:
                current_score += 1
                restricted_score += 1
            else:
                current_score = restricted_score + 1
                restricted_score = 0
            best_score = max(best_score, current_score)
        return best_score
