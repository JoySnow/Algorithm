"""
https://leetcode.com/problems/reverse-integer/description/

-2147483648, 2147483647
[-2^31 , 2^31 - 1]
[-2^31, -1] + [0, 2^31 - 1]

Even if we have the -2147483648 as input,
  the reverse result is overfloat.
If we have the -8463847412 as input,
  the reverse result should be just (-2^31),
  but the Except Answer is funny. :D
So , never mind this.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # get the sign flag
        s = 1 if x >0 else -1
        # all positive
        x = x * s

        rst=int(str(x)[::-1])
        return (rst < 0x7FFFFFFF) * rst * s

