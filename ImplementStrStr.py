class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        m = len(needle)
        n = len(haystack)
        if m==0:
            return haystack
        def compute_fail(needle,next):
            next[0]=-1
            j = -1
            for i in xrange(1,m):
                while j!=-1 and needle[i]!=needle[j+1]:
                    j=next[j]
                if needle[i]==needle[j+1]:
                    j+=1
                next[i]=j
        
        next = [-1]*m
        compute_fail(needle,next)
        j = -1
        for i in xrange(n):
            while j!=-1 and haystack[i]!=needle[j+1]:
                j = next[j]
            if haystack[i]==needle[j+1]:
                j+=1
                if j==m-1:
                    return haystack[i-m+1:]
        return None
