"""
URL: https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution(object):
    def rotate_stupid_way(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        Loop only for half of N, each i stand for a circle in matrix.
            if N%2 == 1, range for [0, N/2)
            if N%2 == 0, range for [0, N/2)
        So, range for [0, N/2) .

        [[1,2,3],
         [4,5,6],
         [7,8,9]],

        H = N - x*2     # 行为x,一边有 （N - x*2）个item
        Corner = N-x-1  # 对角下标
        left = 1, 4     # [i][j], i in [x, H-1), j=x
        down = 7, 8     # [i][j], i=N-x-1, j in [x, H-1)
        right = 9, 6    # [i][j], i in [H-1, x, -1), j=N-x-1
        up = 3, 2       # [i][j], i=x, j in [H-1, x, -1)
        """

        N = len(matrix)
        if N <= 1:
            return

        M = N / 2

        for x in xrange(M):
            H = N - x*2
            Corner = N-x-1  #对角下标

            tmp_left = []
            for i in range(x, x+H-1):  # loop for left
                tmp_left.append(matrix[i][x])  # add left to tmp_left
                matrix[i][x] = matrix[Corner][i]  # copy down to left

            tmp_left = tmp_left[::-1]  # reverse tmp_left for later assignment

            tmp_right = []
            for i in range(x+H-1, x, -1):  # loop for right
                tmp_right.append(matrix[i][Corner])  # add right to tmp_right
                matrix[i][Corner] = matrix[x][i]  # copy up to left
                matrix[x][i] = tmp_left[i-x-1]  # assign tmp_left to up

            for i in range(x, x+H-1):
                matrix[Corner][i] = tmp_right[i-x]  # assign tmp_right to down


    def rotate_clever_way(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        Refer to
        https://leetcode.com/problems/rotate-image/discuss/19123/6-lines-of-code-and-with-O(1)-space-in-c++
        """
        N = len(m)
        if N <= 1:
            return

        for i in range(N):
            for j in range(i):
                m[i][j], m[j][i] = m[j][i], m[i][j]

        for i in range(N):
            m[i] = m[i][::-1]

        return
