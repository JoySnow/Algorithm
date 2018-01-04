"""
https://leetcode.com/problems/move-zeroes/description/
Mine way is pretty good. Same as the best in solution.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = -1
        N = len(nums)
        j = 0

        while(j<N):

            if nums[j] != 0:
                i += 1
                # WAY2: no need to swap, but worse that WAY1
                #if i != j:
                #    nums[i], nums[j] = nums[j], nums[i]

                # WAY1: just swap it, even if i==j
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        print nums

s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
s.moveZeroes([2, 1])
s.moveZeroes([2, 1, 0])
s.moveZeroes([1, 0, 2])
