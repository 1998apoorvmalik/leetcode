__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"

# link: https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dfs_order = []

        def _dfs(node):
            if node is None:
                return
            _dfs(node.left)
            _dfs(node.right)
            dfs_order.append(node)

        _dfs(root)

        dp, best = {}, 1
        dp[None] = [0, 0]
        for node in dfs_order:
            left = dp[node.left]
            right = dp[node.right]
            dp[node] = [1 + max(left[0], right[0]), 1 + left[0] + right[0]]
            best = max(best, max(dp[node]))

        return best - 1
