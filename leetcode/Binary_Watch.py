"""
https://leetcode.com/submissions/detail/135608502/
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num >= 9:
            return []

	def initTable(n):
            res = [[] for i in xrange(0, 7)]
            res[0].append(0)
            bt = [0,]
            i = 1
            while i <= n:
                cnt_one = bt[i/2] + (i&1)
                bt.append(cnt_one)
                res[cnt_one].append(i)
                i += 1
            return res

        bittable = initTable(59)

        res = []
        for i in xrange(0, num+1):
            j = num - i
            if i <= 4 and j <= 6:
                pi = bittable[i]
                pj = bittable[j]
                for h in pi:
                    if h < 12:
                        for m in pj:
                            time_m = ('0' + str(m)) if m < 10 else str(m)
                            res.append("%s:%s" % (h, time_m))
        return res

s = Solution()
ans = ["1:31","1:47","1:55","1:59","2:31","2:47","2:55","2:59","3:15","3:23","3:27","3:29","3:30","3:39","3:43","3:45","3:46","3:51","3:53","3:54","3:57","3:58","4:31","4:47","4:55","4:59","5:15","5:23","5:27","5:29","5:30","5:39","5:43","5:45","5:46","5:51","5:53","5:54","5:57","5:58","6:15","6:23","6:27","6:29","6:30","6:39","6:43","6:45","6:46","6:51","6:53","6:54","6:57","6:58","7:07","7:11","7:13","7:14","7:19","7:21","7:22","7:25","7:26","7:28","7:35","7:37","7:38","7:41","7:42","7:44","7:49","7:50","7:52","7:56","8:31","8:47","8:55","8:59","9:15","9:23","9:27","9:29","9:30","9:39","9:43","9:45","9:46","9:51","9:53","9:54","9:57","9:58","10:15","10:23","10:27","10:29","10:30","10:39","10:43","10:45","10:46","10:51","10:53","10:54","10:57","10:58","11:07","11:11","11:13","11:14","11:19","11:21","11:22","11:25","11:26","11:28","11:35","11:37","11:38","11:41","11:42","11:44","11:49","11:50","11:52","11:56"]
res = s.readBinaryWatch(6)
ansset = set(ans)
resset = set(res)
assert ansset == resset

res = s.readBinaryWatch(7)
print res

print s.readBinaryWatch(8)
print s.readBinaryWatch(9)
print s.readBinaryWatch(10)
print s.readBinaryWatch(11)
