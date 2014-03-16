class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        letter={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxzy'}
        if digits=='':
            return [""]
        comb=list(letter[digits[0]])
        for i in xrange(1,len(digits)):
            comb=[x+y for x in comb for y in letter[digits[i]]]
        return comb
