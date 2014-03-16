class Solution:
    # @return a string
    def count(self,s):
        t=''
        cur='0'
        cnt=0
        for n in s:
            if n != cur:
                if cur!='0':
                    t+=str(cnt)+cur
                cur=n
                cnt=1
            else:
                cnt+=1
        t+=str(cnt)+cur
        return t
        
    def countAndSay(self, n):
        s="1"
        for i in xrange(2,n+1):
            s=self.count(s)
        return s
