"""
URL: https://leetcode.com/problems/unique-binary-search-trees/description/

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution(object):
    def numTrees_way2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Enhance Way1 by cut down the half of the calcaulation for each dp[i]
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]

        idx = 3
        while idx <= n:
            dp.append(0)
            idxmin = idx - 1
            for root in range(idx/2):
                dp[idx] += dp[root] * dp[idxmin - root]
            dp[idx] += dp[idx]
            if idx % 2 == 1: # odd case
                dp[idx] += dp[root+1] * dp[root+1]
            idx += 1

        return dp[n]

    def numTrees_way1(self, n):
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]

        idx = 3
        while idx <= n:
            dp.append(0)
            idxmin = idx - 1
            for root in range(idx):
                dp[idx] += dp[root] * dp[idxmin - root]
            idx += 1

        return dp[n]
