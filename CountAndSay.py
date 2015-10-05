class Solution(object):
    def countAndSay(self, n):
        def next(s):
            n = len(s)
            d = [0]+ filter(lambda x:s[x]!=s[x-1],range(1,n)) + [n]
            n = len(d)-1
            x = ''
            for i in xrange(n):
                x += str(d[i+1]-d[i])+s[d[i]]
            return x
        x=str(1)
        for i in xrange(n-1):
            x=next(x)
        return x
