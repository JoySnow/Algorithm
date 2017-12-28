#########################################################################
# For problem:
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
# Date: 2017-12-27
# Auther: XiaoxueWang(JoySnow)
# Detail: Use Binary Search, O( Mlog(N*M) )
#########################################################################

"""
refer to
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/solution/

Since using HeapSort, it will take O( (K+N/2)logN ), well K will be m*n,
so, this may [Time Limit Exceeded] for this problem.

Here, binary search is a better way.
1. All the item (cnt=m*n) are in range 1~m*n randomly.
2. Start the Binary Search:
3. find the very mid number of low~high(1~m*n), this is just a number.
4. let's find how many items(in matrix) are min than this number as cnt_min_than_mid.
5. if cnt_min_than_mid is >= K, so, the Kth is in left part range(contain mid).
6. if cnt_min_than_mid is < K, in right part(not contain mid).
7. Loop 3~6, until low==high, means this low number is exactly same as the Kth in value.

P.s. we can't just stop when cnt_min_than_mid==k:
  eg:
  table value: ... 24, 24, 28, 28 ...
  1~m*n table: ... 24, 25, 26, 27 ...
  cnt_min_than_mid for mid 24~27 are all the same, if it's also == k,
  you can't just return this mid.

As for how to find cnt_min_than_mid:
  use sum([min(mid/i, n) for i in xrange(1, m+1)])
  1, 2, 3, 4
  2, 4, 6, 8
  3, 6, 9, 12
  in above eg, what's cnt_min_than_mid for mid==8?
  let cnt it by row:
  1, 2, 3, 4    : min( 8/1, 4), could be 8, if this is a bigger table, but 4 here.
  2, 4, 6, 8    : min( 8/2, 4), ok, 4
  3, 6          : min( 8/3, 4), just 2
  So, mean of mid/i is just mid>=i*j, let's find j.(before j, all fit)

Time Consume: O( M*log(M*N) )
  M for each cnt_min_than_mid computing;
  log(M*N) times of BS;
Space Consume: O(1), no much value to store.
"""

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == m*n:
            return m*n
        if k == 1:
            return 1

        low, high = 1, m*n
        while low<high:
            mid = (low+high)/2
            cnt_min_than_mid = sum([min(mid/i, n) for i in xrange(1, m+1)])
            if cnt_min_than_mid >= k:
                high = mid
            else:
                low = mid+1
        return low


s = Solution()
assert s.findKthNumber(3, 3, 5) == 3
assert s.findKthNumber(3, 1, 2) == 2
assert s.findKthNumber(9895, 28405, 100787757) == 31666344

