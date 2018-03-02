class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Make sure candidate1 is diff with candidate2.
        Case5 means another diff value occurs, this make a new pair together
        with candidate1 and candidate2.

        Q1: Why not put case3 and case4 at top?
        A1: If so, the candidate1 and candidate2 could be same value even not
            from same index in nums.

        """
        candidate1 = candidate2 = 0
        count1 = count2 = 0
        for num in nums:
            if candidate1 == num: # case1
                count1 += 1
            elif candidate2 == num: # case2
                count2 += 1
            elif count1 == 0: # case3
                candidate1 = num
                print "candidate1 before: ", candidate1
                count1 += 1
            elif count2 == 0: # case4
                candidate2 = num
                print "candidate2 before: ", candidate2
                count2 += 1
            else: # case5
                count1 -= 1
                count2 -= 1

        t1 = t2 = 0
        for num in nums:
            if candidate1 == num:
                t1 += 1
            elif candidate2 == num:
                t2 += 1
        cnt = len(nums)//3
        ret = []
        if t1 > cnt:
            ret.append(candidate1)
        if t2 > cnt:
            ret.append(candidate2)
        return ret

s = Solution()
print s.majorityElement([2,2,1])
print s.majorityElement([2,2,1,1,1])
print s.majorityElement([1, 1, 1, 2, 1, 2, 1, 2, 2])
