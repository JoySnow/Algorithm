"""
https://leetcode.com/problems/reshape-the-matrix/description/
AC.

2 ways to solve:
    1. Treat as 1-D array, find the needed items' range,
       and get the items with mget() as a row in new matrix.
    2. Approach #3 Using division and modulus [Accepted]
But the test times in leetcode, WAY1 is worse than WAY2.
"""


"""
Treat as 1-D array, find the needed items' range,
and get the items with mget() as a row in new matrix.
"""
class Solution1(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        def mget(s, e):
            """
            Return the [s,e+1) range of matrix.
            """
            rows, cols = s/oldc, s%oldc
            rowe, cole = e/oldc, e%oldc
            new_row = []
            if rows == rowe:
                new_row += nums[rows][cols:cole+1]
            else:
                new_row += nums[rows][cols:]
                rows += 1
                while rows < rowe:
                    new_row += nums[rows]
                    rows += 1
                new_row += nums[rows][:cole+1]
            return new_row

        oldr = len(nums)
        if oldr < 1:
            return nums
        oldc = len(nums[0])
        if r * c != oldr * oldc:
            return nums

        new_nums = []
        s = 0
        e = c
        for row in xrange(r):
            new_nums.append(mget(s, e-1))
            s = e
            e += c
        return new_nums


"""
Refer to:
Approach #3 Using division and modulus [Accepted]
"""
class Solution2(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        oldr = len(nums)
        if oldr < 1:
            return nums
        oldc = len(nums[0])
        if r * c != oldr * oldc:
            return nums

        res = []
        new_row = []
        count = 0
        for i in xrange(oldr):
            for j in xrange(oldc):
                if count % c == 0:
                    res.append(new_row)
                    new_row = []
                new_row.append(nums[i][j])
                #res[count / c][count % c] = nums[i][j]
                count += 1
        res.append(new_row)
        return res[1:]
