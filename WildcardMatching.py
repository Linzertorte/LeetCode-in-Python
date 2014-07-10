
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):

        def match_from(i,s,p):
            n = len(p)
            if i+n > len(s):
                return False
            for j in xrange(n):
                if not (p[j]=='?' or p[j]==s[i+j]):
                    return False
            return True

        if '*' not in p:
            if len(s)!=len(p):
                return False
            return match_from(0,s,p)

        l,r=p.index('*'),p.rindex('*')

        #print l+len(p)-r-1

        if len(s)<l+len(p)-r-1:
            return False

        sleft,pleft = s[:l],p[:l]
        sright,pright = s[r-len(p)+1:],p[r-len(p)+1:]
        if r-len(p)+1==0:
            sright,pright = "",""


        if not match_from(0,sleft,pleft):
            return False
        if not match_from(0,sright,pright):
            return False

        if r-len(p)+1==0:
            s,p=s[l:],p[l:]
        else:
            s = s[l:r-len(p)+1]
            p = p[l:r-len(p)+1]

        pp = ""
        for a in p:
            if a=='*' and len(pp)>0 and pp[-1]=='*':
                continue #ignore extra *
            pp += a
        chunks = pp.split('*')[1:-1]
        begin = 0
        m = len(s)
        for chunk in chunks:
            while begin<m and (not match_from(begin,s,chunk)):
                begin += 1
            if begin == m:
                return False
            begin += len(chunk)
        return True
