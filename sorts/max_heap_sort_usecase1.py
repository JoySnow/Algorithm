#########################################################################
# For problem:
# https://leetcode.com/problems/sort-characters-by-frequency/description/
# Date: 2017-12-25
# Auther: XiaoxueWang(JoySnow)
# Detail: Use MaxHeapSort, O(nlogn)
#########################################################################

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        ch = {}  # chat cnt map
        for c in s:
            c_cnt = ch.setdefault(c, 0)
            ch[c] += 1
        net_num = []
        info = {}  #  cnt char map
        for c, v in ch.items():
            net_num.append(v)
            info_list = info.setdefault(v, [])
            info_list.append(c)
        res_cnt = self._heapSort(net_num)
        result = ''
        for cnt in res_cnt:
            c = info[cnt].pop(0)
            result += c*cnt
        return result

    def _heapSort(self, ch):
        leng = len(ch)
        for i in xrange( leng/2-1, -1, -1):
            self._fixDown(ch, i)
        result = []
        for i in xrange(leng-1, 0, -1):
            result.append(ch[0])
            ch[0] = ch[i]
            ch.pop(-1)
            self._fixDown(ch, 0)
        result.append(ch[0])
        return result

    def _fixDown(self, ch, i_cur):
        i = i_cur
        leng = len(ch)
        while i < (leng/2):
            left = i*2 +1
            right = left + 1
            # must has left child
            # assert left < leng
            # means no right child
            if right >= leng:
                bigger = left
            else:
                bigger = left if ch[left]>ch[right] else right
            if ch[bigger] > ch[i]:
                ch[bigger], ch[i] = ch[i], ch[bigger]
                i = bigger
            else:
                break

s = Solution()
print s.frequencySort('abbccc')
print s.frequencySort('tree')
