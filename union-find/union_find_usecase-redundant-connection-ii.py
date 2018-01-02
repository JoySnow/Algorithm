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
        """
        to_return = [-1, -1]
        N = min(len(edges), 3000) + 1
        parent = list(xrange(0, N))
        sz = [1]*N
        for edge in edges:
            u, v = edge
            parent_u = self._find(parent, u)
            parent_v = self._find(parent, v)
            # v has no parent
            # u's parent is v, this new edge is a reverse pointer
            if parent_v != v or parent_u == parent_v:
                to_return = edge
                continue

            parent[parent_v] = parent_u
            sz[parent_u] += sz[parent_v]
            sz[parent_v] = 0

        return to_return

    #T(N) = near to O(1)
    def _find(self, pin, x):
        tmp = []  # compress pass from node to root
        while(pin[x]!=x):
            x = pin[x]
            tmp.append(x)
        for i in tmp:
            pin[i]= x
        return x



s = Solution()
edges1 = [[1,2], [2,3], [3,4], [4,1], [1,5]]
print s.findRedundantDirectedConnection(edges1)
edges2 = [[1,2], [1,3], [2,3]]
print s.findRedundantDirectedConnection(edges2)
