__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # return self.brute_force_solution(nums)
        # return self.multi_dp_solution(nums)
        return self.sliding_window_dp_solution(nums)

    # Time: O(n^2), Space: O(1)
    # Iterate through the array, and for each index, remove the element at that index and then count the
    # maximum consecutive ones. Return the maximum of all these counts.
    def brute_force_solution(self, nums):
        def _count_max_consec_ones(arr):
            curr_streak, max_streak = 0, 0
            for e in arr:
                if e:
                    curr_streak += 1
                else:
                    curr_streak = 0
                max_streak = max(max_streak, curr_streak)
            return max_streak

        best_streak = 0
        for i in range(len(nums)):
            best_streak = max(best_streak, _count_max_consec_ones(nums[:i] + nums[i + 1 :]))
        return best_streak

    # Time: O(n), Space: O(n)
    # Use two arrays to store the maximum consecutive ones to the left and right of each index. Then,
    # iterate through the array and for each index, return the sum of the maximum consecutive ones to
    # the left and right of that index. Return the maximum of all these sums.
    def multi_dp_solution(self, nums):
        dp1, dp2 = [nums[0]], [nums[-1]]
        for i in range(1, len(nums)):
            dp1.append((dp1[-1] + 1) if nums[i] else 0)
        for i in range(len(nums) - 2, -1, -1):
            dp2.append((dp2[-1] + 1) if nums[i] else 0)
        dp2.reverse()

        best = max(dp1[-2], dp2[1])
        for i in range(1, len(nums) - 1):
            best = max(best, dp1[i - 1] + dp2[i + 1])
        return best

    # Time: O(n), Space: O(1)
    # The sliding window is valid if it contains at most one zero. Initially the window length is one.
    # Use two pointers to keep track of the left and right indices of the current window. Use a boolean
    # to keep track of whether a zero has been found in the current window. Iterate through the array
    # and for each index, if the element at that index is a one, then increment the right pointer. If
    # the element at that index is a zero and a zero has not been found in the current window, then
    # increment the right pointer and set the zero found boolean to True. If the element at that index
    # is a zero and a zero has been found in the current window, then increment the left pointer until
    # it reaches a zero, then set zero found boolean to False. Update the maximum size of the window.
    def sliding_window_dp_solution(self, nums):
        left_idx, right_idx, zero_found = 0, 0, not nums[0]
        max_size = 1

        while right_idx < len(nums) - 1:
            if nums[right_idx + 1]:
                right_idx += 1
            elif not zero_found:
                right_idx += 1
                zero_found = True
            else:
                if nums[left_idx] == 0:
                    zero_found = False
                left_idx += 1

            max_size = max(max_size, right_idx - left_idx + 1)
        return max_size - 1
