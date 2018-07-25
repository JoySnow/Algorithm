"""
https://leetcode.com/problems/arranging-coins/description/
AC.
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int

        x * (x+1) / 2 <= n
        """
        l, r = 1, n
        while l < r:
            # [1, 3] => 2
            # [1, 4] => 3
            mid = (l+r+1) / 2
            tmp = mid*(mid+1) / 2
            if tmp == n:
                return mid
            elif tmp < n: # this tmp could be the answer, so not 'l = mid-1'.
                l = mid
            else:
                r = mid-1
        return r

    def way_2(self, n):
        """
        x * (x+1) / 2 <= n
        x*x + x - 2*n <= 0

        x=[-b±√(b²-4ac)]/2a

        x = ( -1 + sqrt(1+8*n) ) / 2
        """
        from math import sqrt
        return int(( sqrt(1+8*n) - 1 ) / 2)
