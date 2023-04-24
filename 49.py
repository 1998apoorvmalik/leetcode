__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/group-anagrams/

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.sol2(strs)

    # approach 1: categorize by sorted string | TC: O(nmlogm) | SC: O(nm)
    def sol1(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for word in strs:
            key = str(sorted(word))
            groups[key].append(word)

        return groups.values()

    # approach 2: categorize by count | TC: O(nm) | SC: O(nm)
    def sol2(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for word in strs:
            key = [0] * 26
            for e in word:
                key[ord("a") - ord(e)] += 1
            groups[str(key)].append(word)

        return groups.values()
