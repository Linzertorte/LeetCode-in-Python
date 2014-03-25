class Solution:
    # @return an integer
    def romanToInt(self, s):
        tb={'I':1,'V':5,'X':10,'L':50, 'C':100, 'D':500, 'M':1000}
        sum=0
        s=s[::-1]
        last=None
        for x in s:
            if last and tb[x]<last:
                sum-=2*tb[x]
            sum+=tb[x]
            last=tb[x]
        return sum
