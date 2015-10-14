class Solution(object):
    def fractionToDecimal(self, n, d):
        ap = ''
        if n*d<0:
            ap,n,d = '-',abs(n),abs(d)
        x = str(n/d)
        n %= d
        y = ''
        rs = []
        while True:
            if n==0: break
            n *= 10
            t = str(n/d)
            if n in rs:
                i = rs.index(n)
                y = y[:i]+'('+y[i:]+')'
                break
            rs.append(n)
            n %= d
            y += t
        return ap+x if len(y)==0 else ap+x+'.'+y
