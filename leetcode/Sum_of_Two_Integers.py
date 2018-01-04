"""
https://leetcode.com/problems/sum-of-two-integers/description/
without + & -
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        while(b!=0):
            res = a ^ b # the result
            m = a & b   # the carry
            a = res
            b = m<<1
        return a

# This C++ code can pass [-1, 1] testcase.
# While it will time limit with python code. DONT know why.
#    int getSum(int a, int b) {
#        int sum = a;
#        
#        while (b != 0)
#        {
#            sum = a ^ b;//calculate sum of a and b without thinking the carry 
#            b = (a & b) << 1;//calculate the carry
#            a = sum;//add sum(without carry) and carry
#        }
#        
#        return sum;
#    }

s.getSum(7, 9)
s.getSum(2, 9)
# can not pass this case
#s.getSum(-1, 1)
