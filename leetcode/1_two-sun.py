"""
https://leetcode.com/problems/two-sum/description/

solution的第三种

hasheach value

循环 list， 如果他的另一半在hash表中 hit
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in xrange(len(nums)):
            c = target - nums[i]
            if c in h:
                return [h[c], i]
            h[nums[i]] = i
