#########################################################################
# For problem:
# https://leetcode.com/problems/friend-circles/description/
# Date: 2017-12-28
# Auther: XiaoxueWang(JoySnow)
# Detail: Use Union-Find, O( N*N )
#########################################################################

class Solution(object):

    #T(N) = O(N*N/2)
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        cnt = N
        pin = list(xrange(0, N))
        sz = [1]*N
        for i in xrange(0, N-1): # 0 ~ N-2
            for j in xrange(i+1, N): # i+1, N-1
                if M[i][j]:
                    cnt -= self._union(pin, i, j, sz)
        return cnt

    #T(N) = near to O(1)
    def _union(self, pin, i, j, sz):
        iin = self._find(pin, i)
        jin = self._find(pin, j)
        if iin != jin:
            # Find out which tree is bigger
            if sz[i] < sz[j]:
                pin[iin] = jin
                sz[jin] += sz[i]
            else:
                pin[jin] = iin
                sz[iin] += sz[j]
            return 1
        return 0

    #T(N) = near to O(1)
    def _find(self, pin, x):
        tmp = []  # compress pass from node to root
        while(pin[x]!=x):
            x = pin[x]
            tmp.append(x)
        for i in tmp:
            pin[i]= x
        return x


matrix = [
 [1,1,0],
 [1,1,0],
 [0,0,1],]
output = 2

matrix2 = [
 [1,1,1],
 [1,1,0],
 [1,0,1]]
output2 = 1

matrix3 = [
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,1,0,1],
[1,0,0,1,0],
[0,0,1,0,1]]
output3 = 3

matrix4 = [
 [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]
output4 = 4


s = Solution()
#print s.findCircleNum(matrix)
#print s.findCircleNum(matrix2)
#print s.findCircleNum(matrix3)
#print s.findCircleNum(matrix4)
