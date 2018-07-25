"""
URL: https://leetcode.com/problems/summary-ranges/description/

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        N = len(nums)
        if N == 0:
            return []
        elif N == 1:
            return [str(nums[0])]

        ret = []
        s = e = nums[0]

        for v in nums[1:]+[nums[0]]:
            if v == e + 1:  # "in range case"
                e = v
            else:  # a new range case
                if s != e:
                    ret.append(str(s)+'->'+str(e))
                else:
                    ret.append(str(s))
                s = e = v
        return ret
