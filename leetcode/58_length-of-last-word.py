"""
https://leetcode.com/problems/length-of-last-word/
AC.
Easy, String
1 Way.
Not reference.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sp = s.rsplit(None, 1)
        return len(sp[-1]) if sp else 0
