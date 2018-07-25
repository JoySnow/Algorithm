"""
URL: https://leetcode.com/problems/reverse-string-ii/description/

Given a string and an integer k, you need to reverse the first k characters
for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

my_reverseStr(24ms) is a little bit better than offical_way_reverseStr(28ms) in runtime.
"""

class Solution(object):
    def my_reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        N = len(s)
        k2 = 2*k
        t = N / k2

        ret = ''
        if t:
            for i in xrange(t):
                offset = k2 * i
                ret += s[offset:offset+k][::-1]
                ret += s[offset+k:offset+k2]

        left = N % k2
        offset = k2 * t
        if left <= k:
            ret += s[offset:][::-1]
        else:
            ret += s[offset:offset+k][::-1]
            ret += s[offset+k:]

        return ret

    def offical_way_reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a = list(s)
        for i in xrange(0, len(a), 2*k):
            a[i:i+k] = a[i:i+k][::-1]
        return ''.join(a)
