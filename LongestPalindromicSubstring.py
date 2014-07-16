
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        n = len(s)
        s = s+'#'+s[::-1]
        m = 0
        for i in xrange(n):
            #even number
            j = 2*n+1-i
            mat = 0
            while i+mat<n and j+mat<len(s) and s[i+mat]==s[j+mat]:
                mat += 1
            if 2*mat>m:
                m = 2*mat
                l = i-mat
                r= i+mat-1
                #print m,l,r
            j = 2*n-i
            mat = 0
            while i+mat<n and j+mat<len(s) and s[i+mat]==s[j+mat]:
                mat += 1
            if 2*mat-1>m:
                m = 2*mat -1
                l = i-mat+1
                r = i+mat-1
        return s[l:r+1]
