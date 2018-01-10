class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
#        i = -1
#        while i < len(cost)-1:
#            if cost[i+1] < cost[i+2]:
#                res += cost[i+1]
#            else:
#                res += cost[i+2]
#
#        v = []
        N = len(cost)
        v = [0, 0,]
        i = 2
        while i < N:
            v.append( min(cost[i-1]+v[i-1], cost[i-2]+v[i-2]) )
            i += 1
        return v[N-1]

