class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordPart(self,s,i,j,dict,cache=None):
        if cache is None:
            cache={}
        if (i,j) in cache:
            return cache[(i,j)]
        if s[i:j] in dict:
            cache[(i,j)]=True
            return True
        for k in xrange(i+1,j):
            if self.wordPart(s,i,k,dict,cache) and self.wordPart(s,k,j,dict,cache):
                cache[(i,j)]=True
                return True
        cache[(i,j)]=False
        return False
    def wordBreak(self, s, dict):
        return self.wordPart(s,0,len(s),dict)
it changedd
I made another change

