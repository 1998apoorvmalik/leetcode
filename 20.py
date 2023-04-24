__author__ = "Apoorv Malik"
__email__ = "malikap@oregonstate.edu"


# link: https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        brack, stack = {")": "(", "}": "{", "]": "["}, []
        for e in s:
            if e == ")" or e == "}" or e == "]":
                if not stack or brack[e] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(e)
        return False if stack else True
