"""
This answer is not acceptted in
https://leetcode.com/problems/validate-binary-search-tree/.
Last unpass testcase is [0, null, -1].
Tested locally, my code works fine if the 'null' is None in TreeNode value.
Wont fix to AC in leetcode for this question.
Just Doc here.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root and root.val:
            l = root.left
            r = root.right
            if l and self._find_max(l) >= root.val:
                print "Left here:"
                return False
            if r and self._find_min(r) <= root.val:
                print "right here: self._find_min(r) is ", self._find_min(r)
                return False

            if not (self.isValidBST(l) and self.isValidBST(l) ):
                print "Child here:"
                return False
        return True

    def _find_min(self, root):
        while root.left:
            root = root.left
        return root.val

    def _find_max(self, root):
        while root.right:
            root = root.right
        return root.val


s = Solution()
l = TreeNode(None, None, None)
r = TreeNode('-1', None, None)
r = TreeNode('0', l, r)
print s.isValidBST(r)
