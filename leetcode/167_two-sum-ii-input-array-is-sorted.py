"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
AC.
"""


# WAY-1: use dict to record the already passed ones.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(numbers)
        d = {}

        i = 0
        while i < N:
            left = target - numbers[i]
            if left not in d:
                d[numbers[i]] = i
            else:
                return [d[left]+1, i+1]
            i += 1


# WAY-2: use Divide-two to find the another part directly.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(numbers)

        for i in xrange(N):
            tmp = target - numbers[i]
            l, r = i+1, N-1
            while l <= r:
                mid = (l + r) / 2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
