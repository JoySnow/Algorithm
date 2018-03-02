class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
#        num = ''
#        while n:
#            num += chr(n % 26 + 64)
#            print "n % 26: ", n % 26
#            print "n/26: ", n/26
#            n /= 26
#        print num
#        #num += chr(n + 64)
#        return num[::-1]
        num = ''
        while n:
            num += chr( (n-1) % 26 + 65)
            print "n % 26: ", n % 26
            print "n/26: ", n/26
            n = (n-1) / 26
        print num
        #num += chr(n + 64)
        return num[::-1]

s = Solution()
print s.convertToTitle(26)
print s.convertToTitle(52)
