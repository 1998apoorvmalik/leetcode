__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/description/

import collections
from typing import List


class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        dp = {}

        for node, (parent_node, weight) in enumerate(edges):
            graph[parent_node].append((node, weight))

        def _solve(node, parent_edge):
            if (node, parent_edge) not in dp:
                dp_val = 0

                for next_node, weight in graph[node]:
                    dp_val += _solve(next_node, False)

                if not parent_edge:
                    total = dp_val
                    for next_node, weight in graph[node]:
                        dp_val = max(dp_val, weight + _solve(next_node, True) + total - _solve(next_node, False))

                dp[(node, parent_edge)] = dp_val
            return dp[(node, parent_edge)]

        return _solve(0, False)
