class Solution(object):
    def titleToNumber(self, s):
        hs = map(lambda c:ord(c)-ord('A')+1,s)
        return reduce(lambda x,h: x*26+h, hs, 0)
