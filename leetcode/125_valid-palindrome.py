"""
https://leetcode.com/problems/valid-palindrome/description/
AC.
easy, strings
2 ways.
"""

class Solution(object):
    def stupid_way_isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        up = len(s) - 1
        i, j = 0, up
        while i < j:
            while i <= up and not s[i].isalnum():
                i += 1
            
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i > up and j < 0:
                return True
            elif i <= up and j >= 0:
                li = s[i].lower()
                lj = s[j].lower()
                if i >= j:
                    return True
                elif li != lj:
                    return False
                else:
                    i += 1
                    j -= 1
            else:
                return False
        return True

    def better_way_isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i == j:
                return True
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
