#########################################################################
# For problem:
# https://leetcode.com/problems/redundant-connection-ii/description/
# Date: 2018-01-02
# Auther: XiaoxueWang(JoySnow)
# Detail: Use Union-Find, O( N*N )
#########################################################################

class Solution(object):

    #T(N) = O(N*N/2)
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        1. no circle
        2. only one tree
        3. one node has multi parents, in-order is not 1
        4. 1 & 2, a graph with a circle in a tree
        """

        #N = 100001
        N = 10
        parent = list(xrange(0, N))
        flag = False
        nodes = set()
        for edge in edges:
            u, v = edge
            parent_u = self._find(parent, u)
            parent_v = self._find(parent, v)
            print "pu, pv, u, v: ", parent_u, parent_v, u, v
            # v has no parent
            # u's parent is v, this new edge made it a circle.
            if parent_v != v or parent_u == parent_v:
                flag = True
                break
            parent[v] = u
            nodes.add(u)
            nodes.add(v)

        roots = 0
        for i in nodes:
            if self._find(parent, i) == i:
                roots += 1
        if roots != 1:
            flag = True

        print "before return parent: ", parent
        if flag:
            return "Not a tree, False!"
        return "Is a Tree!"

    #T(N) = near to O(1)
    def _find(self, pin, x):
        print "1 pin: x: ", pin, x
        tmp = []  # compress pass from node to root
        while(pin[x]!=x):
            x = pin[x]
            tmp.append(x)
        for i in tmp:
            pin[i]= x
        print "2 pin: x: ", pin, x
        return x



s = Solution()
edges1 = [[1,2], [2,3], [3,4], [4,1], [1,5]]
print s.findRedundantDirectedConnection(edges1)
edges2 = [[1,2], [1,3], [2,3]]
print s.findRedundantDirectedConnection(edges2)

edges3 = [[6,8],[5, 3],[  5, 2],[ 6, 4], [5, 6]]
print s.findRedundantDirectedConnection(edges3)

#8 1  7 3  6 2  8 9  7 5
#7 4  7 8  7 6  0 0
#
edges4 = [[3,8],[6, 8],[  6, 4],[ 5, 3], [5, 6], [5,2]]
print s.findRedundantDirectedConnection(edges4)
#3 8  6 8  6 4
#5 3  5 6  5 2  0 0
