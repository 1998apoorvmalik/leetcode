__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string


class Solution:
    def get_ptable(self, string):
        ptable, i, j = [0] * (len(string) + 1), 0, 1
        while j < len(string):
            if string[i] == string[j]:
                ptable[j] = i + 1
                i += 1
                j += 1
            elif i > 0:
                i = ptable[i - 1]
            else:
                j += 1
        return ptable

    def strStr(self, haystack: str, needle: str) -> int:
        ptable, i, j = self.get_ptable(needle), 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
                if j == len(needle):
                    return i - j
            elif j > 0:
                j = ptable[j - 1]
            else:
                i += 1

        return -1
