"""
Q:153 https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums) - 1
        lo = 0
        hi = N

        if N == 0 or nums[lo] < nums[hi]:
            return nums[lo]

        while lo < hi:
            mid = (lo + hi) / 2

            # left has the hit
            if nums[lo] > nums[mid]:
                hi = mid
            # right has the hit
            elif nums[mid+1] > nums[hi]:
                lo = mid + 1
            # the minor lo is the hit
            else:
                return min( nums[lo], nums[mid+1] )




