"""
In report of https://leetcode.com/problems/fizz-buzz:
    Way3 < Way2 < Way1
    Way3 is the best, not know way.
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        # Way 2: not using %
        # refer https://leetcode.com/problems/fizz-buzz/discuss/89931/
        fizz = buzz = 0
        for v in xrange(1, n+1):
            fizz += 1
            buzz += 1
            if fizz == 3 and buzz == 5:
                fizz = buzz = 0
                res.append("FizzBuzz")
            elif fizz == 3:
                fizz = 0
                res.append("Fizz")
            elif buzz == 5:
                buzz = 0
                res.append("Buzz")
            else:
                res.append(str(v))

        # Way 1: Want to use this way in first try.
        #       Try to avoid multi-calculation of % .
        for v in xrange(1, n+1):
            flag3 = 3 if v % 3 else 0
            flag5 = 5 if v % 5 else 0
            flag = flag3 + flag5
            res.append( "FizzBuzz" if flag == 8 else
                        "Buzz" if flag == 5 else
                        "Fizz" if flag == 3 else
                        str(v))

        # Way3: The most common way
        for v in xrange(1, n+1):
            res.append( "FizzBuzz" if not v % 3 and not v % 5 else
                        "Buzz" if not v % 5 else
                        "Fizz" if not v % 3 else
                        str(v))

        return res


"""
Given testcase:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
