"""
B-tree
Follow Chap18 of <Intro to Algo>
Simple functions:
    insert, delete, search
Author: Xiaoxue Wang
Time: 2018-02-07
"""

import logging

FORMAT = '%(asctime)s - %(levelname)s: %(funcName)s():%(lineno)d:\t%(message)s'
logging.basicConfig(filename="bt.log",
                    level=logging.DEBUG,
                    format=FORMAT)

class TreeNode(object):
    def __init__(self, leaf=False):
        self.n = 0
        self.key = [0,]  # n
        self.child = [0,]  # n+1
        self.leaf = leaf


class BTree(object):
    def __init__(self, t=2):
        self.t = t
        self.create()

    def search(self, x, k):
        """
        :type root: TreeNode
        :rtype: bool
        """
        i = 1
        while i <= x.n and k > x.key[i]:
            i += 1
        if i <= x.n and k == x.key[i]:
            return (x, i)
        elif x.leaf:
            print "In search of %s : Not found!" % k
            return None
        else: # DISK-READ(x, x.child[i])
            return self.search(x.child[i], k)

    def create(self):
        n = TreeNode(leaf=True)
        self.root = n
        #DISK-WRITE(n)

    def insert(self, k):
        print "Insert ", k
        r = self.root
        if r.n == 2*self.t-1:
            s = TreeNode()
            self.root = s
            s.child.append(r)
            self._split_child(s, 1)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

    def _split_child(self, x, i):
        t = self.t

        y = x.child[i]
        z = TreeNode()
        z.leaf = y.leaf
        z.n = y.n = t - 1

        for j in xrange(t+1, 2*t):
            z.key.append( y.key[j] )

        if not y.leaf:
            for j in xrange(t+1, 2*t+1):
                z.child.append( y.child[j] )
            y.child = y.child[:t+1]


        x.key.append(x.key[x.n])
        for j in xrange(x.n, i-1, -1):
            x.key[j+1] = x.key[j]
        x.key[i] = y.key[t]
        x.n += 1
        x.child.append(z)

        y.key = y.key[:t]

        #DISk-WRITE(x)
        #DISk-WRITE(y)
        #DISk-WRITE(z)

    def _insert_nonfull(self, x, k):
        i = x.n
        if x.leaf:
            x.key.append(x.key[i])
            while i > 0 and k < x.key[i]:
                x.key[i+1] = x.key[i]
                i -= 1
            x.key[i+1] = k
            x.n += 1
            #DISK-WRITE(x)
        else:
            while i > 0 and k < x.key[i]:
                i -= 1
            i = i + 1
            #DISK-READ(x.child[i])
            if x.child[i].n == 2*self.t-1:
                self._split_child(x, i)
                if k > x.key[i]:
                    i += 1
            self._insert_nonfull(x.child[i], k)


    def delete(self, k):

        print "Delete ", k
        r = self.root
        if not r:
            print "Empty tree!"
            return

        # r.n in [1, 2t-1]
        if r.n == 1:
            if r.leaf:
                if r.key[1] == k:
                    self.root = None
                else:
                    print "Delete key not found!"
            elif r.child[1].n < self.t and r.child[2].n < self.t:
                # merge root with child, tree-height --
                self._merge_child(r, 1)
                r = self.root = r.child[1]

        self._delete_r(r, k)


    def _delete_r(self, x, k):
        self.print_tree()
        i = x.n
        while i > 0 and k < x.key[i]:
            i -= 1

        if k == x.key[i]:
            if x.leaf:
                # case 1: leaf
                logging.debug('delete case 1')
                for j in xrange(i, x.n):
                    x.key[j] = x.key[j+1]
                x.key.pop()
                x.n -= 1
            else:
            # case 2: not leaf
                logging.debug('delete case 2')
                if x.child[i].n >= self.t:
                    # case 2a:
                    logging.debug('delete case 2a')
                    x.key[i] = self._delete_max(x.child[i])
                elif x.child[i+1].n >= self.t:
                    # case 2b
                    logging.debug('delete case 2b')
                    x.key[i] = self._delete_min(x.child[i+1])
                else:
                    # case 2c: merge child[i] and child[i+1]
                    logging.debug('delete case 2c')
                    self._merge_child(x, i)
                    self._delete_r(x.child[i], k)
        else:
            i += 1
            # case 3: k in child
            logging.debug('delete case 3')
            if x.child[i].n < self.t:
                if i-1 >= 1 and x.child[i-1].n >= self.t:
                    # case 3a-left: borrow from left sibling
                    logging.debug('delete case 3a-left')
                    self._borrow_from_left(x, i)
                elif i+1 <= x.n+1 and x.child[i+1].n >= self.t:
                    # case 3a-right: borrow from right sibling
                    logging.debug('delete case 3a-right')
                    self._borrow_from_right(x, i)
                else:
                    # case 3b: merge with a sibling
                    logging.debug('delete case 3b')
                    if i-1 >= 1:
                        print "DEBUG: been here?"
                        self._merge_child(x, i-1)
                        i -= 1
                    else:
                        self._merge_child(x, i)

            self._delete_r(x.child[i], k)

    def _delete_min(self, x):
        """
        Return the deleted value
        """
        if x.leaf:
            minkey = x.key[1]
            for j in xrange(1, x.n):
                x.key[j] = x.key[j+1]
            x.key.pop()
            return minkey

        if x.child[1].n < self.t:
            if x.child[2].n >= self.t:
                self._borrow_from_right(x, 1)
            else:
                self._merge_child(x, 1)

        return self._delete_min(x.child[1])

    def _delete_max(self, x):
        """
        Return the deleted value
        """
        if x.leaf:
            return x.key.pop()

        if x.child[x.n+1].n < self.t:
            if x.child[x.n].n >= self.t:
                self._borrow_from_left(x, x.n+1)
            else:
                self._merge_child(x, x.n)

        return self._delete_max(x.child[x.n+1])



    def _borrow_from_right(self, x, i):
        """
        Borrow x.child[i+1]'s min key to x.child[i].
        child[i] and child[i+1] must exist.
        """
        y = x.child[i]
        z = x.child[i+1]

        y.key.append(x.key[i])
        x.key[i] = z.key[1]
        for j in xrange(1, z.n):
            z.key[j] = z.key[j+1]
        z.key.pop()

        if not y.leaf:
            y.child.append(z.child[1])
            for j in xrange(1, z.n+1):
                z.child[j] = z.child[j+1]
            z.child.pop()

        y.n += 1
        z.n -= 1

    def _borrow_from_left(self, x, i):
        """
        Borrow x.child[i-1]'s max key to x.child[i].
        child[i-1] and child[i] must exist.
        """
        y = x.child[i-1]
        z = x.child[i]

        z.key.append(z.key[z.n])
        for j in xrange(z.n+1, 1):
            z.key[j] = z.key[j-1]
        z.key[1] = x.key[i-1]
        x.key[i-1] = y.key[y.n]
        y.key.pop()

        if not z.leaf:
            z.child.append(None)
            for j in xrange(z.n+2, 1):
                z.child[j] = z.child[j-1]
            z.child[1] =  y.child[y.n+1]
            y.child.pop()

        z.n += 1
        y.n -= 1


    def _merge_child(self, x, i):
        """
        Merge x.child[i] with x.child[i+1].
        child[i] and child[i+1] must exist.
        """
        y = x.child[i]
        z = x.child[i+1]

        y.key.append(x.key[i])
        y.key += z.key[1:]
        if not y.leaf:
            y.child += z.child[1:]
        y.n += 1
        y.n += z.n
        # Remove z in DISK

        for j in xrange(i, x.n):
            x.key[j] = x.key[j+1]
        x.key.pop()
        for j in xrange(i+1, x.n+1):
            x.child[j] = x.child[j+1]
        x.child.pop()
        x.n -= 1




    def print_tree(self):
        print "======Print Tree========"
        h = self.root
        if not h:
            print "Empty tree!"
            return

        level = [h,]
        while level:
            new_level = []
            print_this_level = ''
            for n in level:
                print_this_level += "%s\t" % (n.key[1:])
                if not n.leaf:
                    new_level += n.child[1:]
            print "BT: ", print_this_level
            level = new_level



def test_normal():
    """
    Test-case-1: pass
    """
    bt = BTree(t=2)
    bt.print_tree()
    v = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    for item in v:
        bt.insert( item )
        bt.print_tree()

    for item in v[::-1]:
        bt.delete( item )
        bt.print_tree()

def test_delete():
    """
    Test-case-2: All delete cases tested
    """
    bt = BTree(t=2)
    bt.print_tree()
    v = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    for item in v:
        bt.insert( item )
        bt.print_tree()

    # test delete-case-3a-right
    bt.delete('B')
    bt.print_tree()

    # test delete-case-3a-left
    bt.delete('E')
    bt.print_tree()

    # test delete-case-2b
    bt.delete('H')
    bt.print_tree()

    # test delete-case-2a
    bt.insert('E')
    bt.print_tree()
    bt.insert('B')
    bt.print_tree()
    bt.delete('C')
    bt.print_tree()

    bt.insert('C')
    bt.print_tree()
    bt.delete('F')
    bt.print_tree()

def test_insert():
    bt = BTree(t=2)
    bt.print_tree()

    bt.insert('F')
    bt.insert('I')
    bt.insert('I')


test_normal()
test_delete()
