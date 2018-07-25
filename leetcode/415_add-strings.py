"""
https://leetcode.com/problems/add-strings/description/
AC.
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        Na = len(num1)
        Nb = len(num2)
        N, t, NL = (Na, num2, Nb) if Na < Nb else (Nb, num1, Na)
        res = []

        carry = 0
        for i in xrange(1, N+1):
            s = carry + int(num1[-i]) + int(num2[-i])
            carry = s / 10
            res.append(str(s % 10))

        for i in range(N+1, NL+1):
            s = carry + int(t[-i])
            carry = s / 10
            res.append(str(s % 10))

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])
