import Queue


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_a_basic_n_level_tree(n):
    """
    :type n: int
    :rtype: TreeNode
    """
    if n <= 0:
        return None

    root = TreeNode(1)
    if n == 1:
        return root

    q = Queue.Queue()
    q.put(root)
    last_level_cnt = pow(2,n-1)
    val = 2
    while not q.empty() and q.qsize() < last_level_cnt:
        c = q.get()
        l, r = TreeNode(val), TreeNode(val+1)
        c.left, c.right = l, r
        q.put(l)
        q.put(r)
        val += 2
    return root


def print_tree(root):
    """
    :type root: TreeNode
    :rtype: None
    """
    print "======Print Tree========"
    h = root
    if not h:
        print "Empty tree!"
        return

    level = [h,]
    while level:
        new_level = []
        print_this_level = ''
        for n in level:
            print_this_level += "%s\t" % (n.val)
            if n.left:
                new_level.append(n.left)
                if n.right:
                    new_level.append(n.right)
        print "BT: ", print_this_level
        level = new_level


if __name__ == "__main__":
    pass
