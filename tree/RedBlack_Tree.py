"""
LLRBT, refer to http://www.cs.princeton.edu/~rs/talks/LLRB/RedBlack.pdf .
"""

#TODO: just finish the deleteMax, need go on with deleteMin and delete.

class TreeNode(object):
    """
    Color: True for Red, False for Black.
    """
    def __init__(self, value, color=True, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.color = color

class RedBlackTree(object):

    def __init__(self):
        self.root = None

    def insert_value(self, value):
        if not self.root:
            self.root = TreeNode(value, False)
        else:
            self.root = self._insert_value(self.root, value)
            self.root.color = False

    def _insert_value(self, h, value):
        if h is None:
            return TreeNode(value, color=True)
        # insert at bottom/leaf

        if self._is_red(h.left) and self._is_red(h.right):
            self._color_flip(h)
        # split this 4-node h on the way **down**
        # Why?
        # Since we are going to insert a node under h,
        # make the preparation(split 4-node) first before insert it.

        if value == h.value:
            print "Same value %s is already in Tree." % value
        elif value < h.value:
            h.left = self._insert_value(h.left, value)
        else:
            h.right = self._insert_value(h.right, value)

        if self._is_red(h.right):
            h = self._left_rotate(h)
        # Fix right-leaning reds on the way **up**

        if self._is_red(h.left) and self._is_red(h.left.left):
            h = self._right_rotate(h)
        # Fix two reds in a row on the way **up**

        return h

    def _is_red(self, h):
        return h.color if h else False

    def _color_flip(self, h):
        tmp = h.color
        h.color = h.left.color
        h.left.color = h.right.color = tmp

    def _left_rotate(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = True
        return x

    def _right_rotate(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = True
        return x

#    def remove_value(self, value):
#        h = self.find_value(value)
#        if not h:
#           print "Nothing to remove!"
#           return
#
#        self._remove_value(self.root, value)
#
#
#    def _remove_value(self, h, value):
#        # Turn Left
#        if value < h.value:

    def _delete_max(self, h):
        if self._is_red(h.left):
            h = self._right_rotate(h)
        # lean 3-node to right

        if not h.right:
            return
        # Remove node on bottom, this h must be RED.

        if (not self._is_red(h.right)) and (not self._is_red(h.right.left)):
            h = self._moveRedRight(h)
        # In this case:
        # h.right is black, h.right not connect with h;
        # h.right.left is black, then h.right.right must be black. (LLRBT)
        # So, this h.right node is a 2-node,
        # have to borrow from his parent or sibiling.

        # be sure that h.right is RED.
        h.right = self._delete_max(h.right)

        h = self._fixup(h)
        # fix right-leaning red links and eliminate 4-nodes on the way up
        return h

    def delete_max(self):
        if self.root:
            self.root = self._delete_max(self.root)
        else:
            print "Empty Treem, Nothing to remove!"

    def _moveRedRight(self, h):
        """
        For the 2-node h.right, try to borrow from his parent or sibiling.
        In the easy case:
            h.left.left is black, means:
            h.right node's sibiling is a 2-node, can not help with our h.right.
            So, we just borrow from parent. make it a 4-node.
        In the harder case:
            h.left.left is red, means:
            h.right node's sibiling is at least a 3-node,
            so it can borrow one to h.rightr.
            here, we colorflip first, make it a 5-node,
            then rotate-right and flipcolor back, combine a parent to a 3-node,
            and borrow one from silbiling as parent again.
        """
        self._color_flip(h)
        if self._is_red(h.left.left):
            h = self._right_rotate(h)
            self._color_flip(h)
        return h

    def _fixup(self, h):
        if self._is_red(h.right):
            h = self._left_rotate(h)
        # rotate-left right-leaning reds

        if self._is_red(h.left) and self._is_red(h.left.left):
            h = self._right_rotate(h)
        # rotate-right red-red pairs

        if self._is_red(h.left) and self._is_red(h.right):
            self._color_flip(h)
        # split 4-node

        return h




    def find_value(self, value):
        h = self.root
        if not h:
           print "Empty tree, not found!"
           return None

        while value != h.value:
            if value < h.value:
                if not h.left:
                    print "Stop at %s, cannt find value %s." % (h.value, value)
                    return None
                h = h.left
            else:
                if not h.right:
                    print "Stop at %s, cannt find value %s." % (h.value, value)
                    return None
                h = h.right
        return h


    def print_tree(self):
        print "======Print Tree========"
        h = self.root
        level = [h,]
        while level:
            new_level = []
            print_this_level = ''
            for n in level:
                if n:
                    print_this_level += "%s %s\t" % (n.value, n.color)
                    new_level.append(n.left)
                    new_level.append(n.right)
                else:
                    print_this_level += "Null\t"
            print print_this_level
            level = new_level



rbt = RedBlackTree()
rbt.print_tree()
for item in ['A', 'B', 'C', 'D', 'E', 'F']:
    rbt.insert_value( item )
    rbt.print_tree()

rbt.delete_max()
rbt.print_tree()
rbt.delete_max()
rbt.print_tree()
