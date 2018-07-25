"""
https://leetcode.com/problems/rotate-array/description/
AC.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k < 1:
            return
        N = len(nums)

        cnt = 0 # cnt for the resetted item counts

        for i in xrange(1, k+1):
            if cnt >= N:
                break
            "i is the to replaced index in array"
            source_i = N-i
            target_i = ( source_i + k ) % N
            print "I: ", i, source_i, target_i
            while target_i != source_i:
                nums[target_i], nums[source_i] = nums[source_i], nums[target_i]
                cnt += 1
                target_i = (target_i + k) % N
            cnt += 1  # By using source_i as a tmp, a last swap is reduced here.

        return
