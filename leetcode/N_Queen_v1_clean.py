"""
For Question:
    https://leetcode.com/problems/n-queens/description/
Code submitted at:
https://leetcode.com/submissions/detail/135471994/
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        matrix = []
        leftj = set(xrange(0, n))
        self._check(n, matrix, 0, leftj, res)
        return res


    def _check(self, n, matrix, i, leftj, res):
        # already placed N queens.
        if i == n:
            # assert leftj is None
            mm = [''.join(l) for l in matrix]
            res.append(mm)
            return

        import copy
        for j in leftj:
            if self._isValid(n, matrix, i, j):
                to_add = ['.' for index in xrange(n)]
                to_add[j] = 'Q'
                matrix.append(to_add)
                new_leftj = copy.deepcopy(leftj)
                new_leftj.remove(j)
                self._check(n, matrix, i+1, new_leftj, res)
                # remove the added new line in matrix
                matrix.pop()

    def _isValid(self, n, matrix, i, j):
        # up-left to low-right line
        for x in xrange(0, i):
            # i-j = x-y
            y = x - (i-j)
            if 0 <= y < n:
                if matrix[x][y] == 'Q':
                    return False

        # low-left to up-right line
        for x in xrange(0, i):
            y = i+j - x
            if 0 <= y < n:
                if matrix[x][y] == 'Q':
                    return False

        return True

s = Solution()
print s.solveNQueens(5)
