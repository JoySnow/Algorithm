"""
URL: https://leetcode.com/problems/different-ways-to-add-parentheses/description/

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

"""



class Solution(object):
    def WAY_1_diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]

        l1 = 2 * 3 - 4 * 5,         1 3 5
        l1 = 2 * (3 - 4) * 5        1 3
        l1 = (2 * (3 - 4)) * 5      1
        """
        N = len(input)
        if N == 0:
            return [0]

        a = []
        tmp = []
        for v in input:
            if v in ('*', '-', '+'):
                a.append(''.join(tmp))
                tmp = []
                a.append(v)
            else:
                tmp.append(v)
        if tmp:
            a.append(''.join(tmp))

        if len(a) == 1:
            return [int(input)]

        ret = set()

        def _construct(a, cnt):
            if cnt == 1:
                ret.add(''.join(a))
                return

            for i in range(cnt):
                index = i * 2 + 1
                cur_a = a[:index]
                cur_a[index-1] = '(' + a[index-1] +  a[index] + a[index+1] + ')'
                cur_a += a[index+2:]
                _construct(cur_a, cnt-1)

        cnt = len(a) / 2
        _construct(a, cnt)
        return [eval(s) for s in ret]


    def WAY_2_diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]

        Refer to
        (https://leetcode.com/problems/different-ways-to-add-parentheses
        /discuss/66331/C++-4ms-Recursive-and-DP-solution-with-brief-explanation)
        """
        OPS = ('*', '+', '-')
        ret = []

        for i in range(len(input)):
            op = input[i]
            if op in OPS:
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                for lv in l:
                    for rv in r:
                        if op == OPS[0]:
                            ret.append(lv * rv)
                        elif op == OPS[1]:
                            ret.append(lv + rv)
                        else:
                            ret.append(lv - rv)
        if not ret:
            ret.append(int(input))
        return ret
