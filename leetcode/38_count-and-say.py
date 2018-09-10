"""
https://leetcode.com/problems/count-and-say/description/
AC.
1 Way.
Not reference.
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def cas(s):
            res = []
            tmp = None
            cnt = 0
            for c in s:
                if not tmp:
                    tmp, cnt = c, 1
                elif c == tmp:
                    cnt += 1
                else:
                    res.append(str(cnt) + tmp)
                    tmp, cnt = c, 1
            if tmp:
                res.append(str(cnt) + tmp)
            return ''.join(res)
            
        res = '1'
        for i in range(n-1):
            res = cas(res)
        return res
