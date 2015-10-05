class Solution(object):
    def reverseBits(self, n):
        x = 0
        for i in xrange(32):
            x = x*2+(n%2)
            n/=2
        return x
