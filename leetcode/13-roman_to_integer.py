"""
https://leetcode.com/problems/roman-to-integer/description/
AC.
2 ways.
"""

class Solution(object):
    def Logical_Way_romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def cal(vals):
            # Case-1: all vals are same
            if vals[-1] == vals[-2]:
                return len(vals)*vals[-1]

            # Case-2: vals are decreasing
            tmp = vals[-1] * 2
            for v in vals[::-1]:
                tmp -= v
            return tmp

        m = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
        """
        Logical Way:
        MCMXCIV
        1000   100 1000   10 100   1 5
        1000 | 100 1000 | 10 100 | 1 5 |
        1000 | 900      | 90     | 4   |
        1994
        """
        res = 0
        tmp = []
        for c in s:
            v = m[c]
            if not tmp:
                tmp = [v, ]
            elif v >= tmp[-1]:  # include both Case-1 & Case-2
                tmp.append(v)
            else:
                res += cal(tmp) if len(tmp) > 1 else tmp[0]
                tmp = [v, ]
        res += cal(tmp) if len(tmp) > 1 else tmp[0]
        return res

    def Stright_Forward_Way_romanToInt(self, s):
        """
        StrightForward Way:
        MCMXCIV
        1000   100 1000   10    100    1    5
             -    +      -     +     -    +
               900 1900   1890  1990   1989  1994
        """
        res = 0
        for i in xrange(0, len(s)-1):
            a, b = m[s[i]], m[s[i+1]]
            res = res - a if a < b else res + a
        res += m[s[-1]]
        return res
