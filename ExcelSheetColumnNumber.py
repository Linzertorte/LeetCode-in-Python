class Solution(object):
    def titleToNumber(self, s):
        hs = map(lambda c:ord(c)-ord('A')+1,s)
        x = 0
        for h in hs:
            x = x*26+h
        return x
