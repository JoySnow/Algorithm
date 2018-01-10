class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        for j in xrange(0, n):
            matrix = [['.' for i in xrange(n)] for i in xrange(n)]
            matrix[0][j] = 'Q'
            leftj = set(xrange(0, n))
            leftj.remove(j)
            self._check(n, matrix, 1, leftj, res)
        return res


    def _check(self, n, matrix, i, leftj, res):
        # already placed N queens.
        if i == n:
            mm = [''.join(l) for l in matrix]
            res.append(mm)

        import copy
        for j in leftj:
            if self._isValid(n, matrix, i, j):
                matrix[i][j] = 'Q'
                new_leftj = copy.deepcopy(leftj)
                new_leftj.remove(j)
                self._check(n, matrix, i+1, new_leftj, res)

    def _isValid(self, n, matrix, i, j):
        # up-left to low-right line
        for x in xrange(0, i):
            # i-j = x-y
            y = x - (i-j)
            if 0<= y < n:
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
print s.solveNQueens(4)
