class Solution:
    def isMatch(self, s, p):
        def match_from(i,n, s, p):
            m = len(p)
            if i+m > n:return False
            return reduce(lambda x,y: x and y,[p[j]=='?' or p[j]==s[i+j] for j in xrange(m)], True)
        chunks = re.split('\*+',p)
        cnt,n = len(chunks),len(s)
        if cnt == 1:
            return len(s)==len(p) and match_from(0,n,s,p)
        l,r = len(chunks[0]),len(chunks[-1])
        if l + r > n or not match_from(0,l,s,chunks[0]) or not match_from(n-r,n,s,chunks[-1]):
            return False
        begin = l
        n -= r
        for i in xrange(1,cnt - 1):
            chunk = chunks[i]
            while begin<n and (not match_from(begin, n, s,chunk)):
                begin += 1
            if begin == n:
                return False
            begin += len(chunk)
        return True
