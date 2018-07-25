# -*- coding:utf-8 -*-
"""
URL: https://leetcode.com/problems/gray-code/description/

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the
code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""

"""
Int     Binary   Grey Code  Grey Code Num
0　　    000        000     0
1　　    001        001     1
2  　    010        011     1 + 2 = 3
3  　    011        010     0 + 2 = 2
4  　    100        110             2 + 4
5  　    101        111		    3 + 4
6  　    110        101             0 + 4
7  　　  111        100             1 + 4
8       1000       1100

9        1001      1101


WAY-1:
镜面排列:
    n位元的格雷码可以从n-1位元的格雷码以上下镜射后加上新位元的方式快速的得到。
satrt with n = 1, (0, 1), get the values in n=2 level, and go on ...


WAY-2:

二进制码→格雷码（编码）：
此方法从对应的n位二进制码字中直接得到n位格雷码码字，步骤如下：
 1. 对n位二进制的码字，从右到左，以0到n-1编号
 2. 从低位到高位，对相邻做异或。如果二进制码字的第i位和i+1位相同，则对应的格雷
    码的第i位为0，否则为1（当i+1=n时，二进制码字的第n位被认为是0，即第n-1位不变）
eg. 二进制码0101，为4位数, 对应的格雷码为 0111.
    二进制码1010，为4位数, 对应的格雷码为 1111.

格雷码→二进制码（解码）：
  最左边第一位不变。从左边第二位起，将每位与左边一位解码后的值异或，作为该位解码
  后的值。依次异或，直到最低位。
eg. 格雷码为 0111, 对应的二进制码0101.

Refer to:
    http://www.cnblogs.com/grandyang/p/4315649.html
    https://baike.baidu.com/item/%E6%A0%BC%E9%9B%B7%E7%A0%81/6510858?fr=aladdin
"""

class Solution(object):
    def way_1_grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        ret = [0, 1]
        idx = 1
        while idx < n:
            p = pow(2, idx)
            ret += [v+p for v in ret[::-1]]
            idx += 1
        return ret

    def way_2_grayCode(self, n):
        return [(i >> 1) ^ i for i in xrange(pow(2,n))]
