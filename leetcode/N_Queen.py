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
            print "In solve : matrxi", matrix
        return res


    def _check(self, n, matrix, i, leftj, res):
        print "Step in check: "
        print "n, matrix, i, leftj, res: ", n, i, leftj, res
        print "MA: "
        print matrix
        # already placed N queens.
        if i == n:
            # assert leftj is None
            print "In _check: "
            print matrix
            res.append(matrix)

        #for j in xrange(0, n):
        import copy
        for j in leftj:
            if self._isValid(n, matrix, i, j):
                matrix[i][j] = 'Q'
                new_leftj = copy.deepcopy(leftj)
                new_leftj.remove(j)
                self._check(n, matrix, i+1, new_leftj, res)

    def _isValid(self, n, matrix, i, j):
        # up-left to low-right line
        print "========IN _isValid: i, j: ", i, j
        print "xy pair"
        for x in xrange(0, i):
            # i-j = x-y
            y = x - (i-j)
            if 0<= y < n:
                print "x, y: ", x, y
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
