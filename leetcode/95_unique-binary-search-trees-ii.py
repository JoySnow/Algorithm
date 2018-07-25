"""
URL: https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        """
        https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31493/Java-Solution-with-DP

        # IDEA:
        dp[i]: f(1, i), all combinations of [1 ~ i]

        When we have dp[i-1],
        dp[i] = for each j in [1, i]:
                    j is root. left_parts = f(1, j-1), right_parts = f(j+1, i).
                    combine(j, a left_part, a right_part), get a new path for dp[i].
                    the num of such path is len(left_parts) * len(right_parts).

        Here, use dp[j-1] for f(1, j-1), we already got it.
        For f(j+1, i), we don have it in dp record.
        But since BST, the value is diff, but the combination of [i]to[j] is always same.
        f(j+1, i) can be get by dp[i-j], and replace each value in it with val+j.

        # Hints:
        1. Q：Why deepcopy for f(j+1, i), but not f(1, j-1)?
           A：After we get dp[i-1], each tree in dp[i-1] is not changed anymore.
              when cal dp[i], we use f(1, j-1) in a referecing way only.
                              but when using f(j+1, i), we need a new tree. So, deepcopy it.
        2. dp[0] should be [None,] .
        3. A better way for getting f(j+1, i): (did'n have code for this version)
            to cal f(1, i), we need each item in matrix f(x, y), where x < y.
            so, when we got f(1, i-1), we cal f(2, i-1) ~ f(i-1, i-1) also.
            After these, when cal f(1, i):
                we can get f(j+1, i) directly from f(j+1, i-1) in the referce way.
                Don't need to clone a Totally new tree from bottom.
                And in this way, we only need to maintian for {f(2, i) ~ f(i, i)} for extral only (except dp[i]).

        """
        dp = [[None,], [TreeNode(1),]]

        if n == 0:
            return []
        if n == 1:
            return dp[n]

        def _construct(r, offset):
            if r:
                tmpr = TreeNode(r.val+offset)
                tmpr.left = _construct(r.left, offset)
                tmpr.right = _construct(r.right, offset)
                return tmpr

        def _printT(r):
            if r:
                print r.val
                _printT(r.left)
                _printT(r.right)

        i = 2
        while i <= n:
            # count for dp[i]
            dp.append([])
            print "> i: ", i
            for j in range(1, i+1):  # j as root
                print ">>> j: ", j
                left_part =dp[j-1]
                right_part = dp[i-j]
                print ">>> j-1: ", j-1
                print ">>> i-j: ", i-j
                print ">>> left_part: ", left_part
                print ">>> right_part: ", right_part
                for la in left_part:
                    for ra in right_part:
                        print ">>>>> la: ", la
                        print ">>>>> ra: ", ra
                        tmpt = TreeNode(j)
                        tmpt.left = la
                        tmpt.right = _construct(ra, j)
                        print ">>>>> tmpt: ", _printT(tmpt)
                        dp[i].append(tmpt)
            i += 1

        return dp[n]
