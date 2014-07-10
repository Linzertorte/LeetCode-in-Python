class Solution:
    # @return a list of integers
    def grayCode(self, n):
        def n_th_gray(n):
            base,ans = 0,0
            while n:
                if n&1:
                    ans += 1<<base
                    ans ^= 0 if base ==0 else 1<<(base-1)
                n>>=1
                base +=1
            return ans
        
        gray = []
        for i in xrange(1<<n):
            gray.append(n_th_gray(i))
        return gray
