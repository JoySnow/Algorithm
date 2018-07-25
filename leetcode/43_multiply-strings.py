"""
https://leetcode.com/problems/multiply-strings/description/
AC.
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if '0' in (num1, num2):
            return '0'

        N1 = len(num1)
        N2 = len(num2)
        if N1 >= N2:
            t_max, t_min = num1, num2
            n_max, n_min = N1, N2
        else:
            t_max, t_min = num2, num1
            n_max, n_min = N2, N1

        res = [0,]

        for i in xrange(1, n_min+1):
            #t_min[-i] * t_max
            m = int(t_min[-i])
            carry = 0
            tmp_res = []
            for j in range(n_max-1, -1, -1):
                s = m * int(t_max[j]) + carry
                carry = s / 10
                tmp_res.append(s % 10)
            if carry:
                tmp_res.append(carry)
            for index in range(i-1):
                tmp_res.insert(0, 0)
            res = self.add(res, tmp_res)

        new_res = [str(v) for v in res]
        return ''.join(new_res[::-1])

    def add(self, num1, num2):
        """
        :type num1: list of reversed int
        :type num2: list of reversed int
        :rtype: list of reversed int
        """
        Na = len(num1)
        Nb = len(num2)
        N, t, NL = (Na, num2, Nb) if Na < Nb else (Nb, num1, Na)
        res = []

        carry = 0
        for i in xrange(N):
            s = carry + num1[i] + num2[i]
            carry = s / 10
            res.append(s % 10)

        for i in range(N, NL):
            s = carry + t[i]
            carry = s / 10
            res.append(s % 10)

        if carry:
            res.append(carry)

        return res
