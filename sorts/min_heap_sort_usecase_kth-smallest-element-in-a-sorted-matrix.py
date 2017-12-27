#########################################################################
# For problem:
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
# Date: 2017-12-27
# Auther: XiaoxueWang(JoySnow)
# Detail: Use MinHeapSort, O( (N/2+K)logN = NlogN )
# Steps:
#   1. Build a minHeap of elements from the first row.
#   2. Find the k min nums by doing the following operations k-1 times :
#        store the root(Top Element in Heap),
#        replace root with the next element from the same column with old root,
#        (so we need to store the row and column info of items in HEAP)
#        if no such element to replace, just reduce the HEAP number.
#########################################################################


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        N = len(matrix)
        if k == N*N:
            return matrix[N-1][N-1]
        if k == 1:
            return matrix[0][0]

        to_sort_v = matrix[0]
        to_sort_i = [0]*N
        to_sort_j = list(xrange(0, N))
        to_sort = zip(to_sort_v, to_sort_i, to_sort_j)

        for i in xrange( N/2-1, -1, -1):
            self._minFixDown(to_sort, i)

        result = []
        for i in xrange(k-1, 0, -1):
            result.append(to_sort[0][0])
            tsi, tsj = to_sort[0][1]+1, to_sort[0][2]
            if 0<=tsi<N:
                to_sort[0] = (matrix[tsi][tsj], tsi, tsj)
            else:
                to_sort[0] = to_sort.pop(-1)
            self._minFixDown(to_sort, 0)
        result.append(to_sort[0][0])
        return result[-1]


    def _minFixDown(self, ch, i_cur):
        i = i_cur
        leng = len(ch)
        while i < (leng/2):
            left = i*2 +1
            right = left + 1
            # must has left child
            # assert left < leng
            # means no right child
            if right >= leng:
                smaller = left
            else:
                smaller = left if ch[left][0]<ch[right][0] else right
            if ch[smaller][0] < ch[i][0]:
                ch[smaller], ch[i] = ch[i], ch[smaller]
                i = smaller
            else:
                break

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
assert matrix[0][2] == 9
s = Solution()
print s.kthSmallest(matrix, k)
