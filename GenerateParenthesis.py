class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        parens=[]
        if n==0:
            return [""]
        for paren in self.generateParenthesis(n-1):
            parens.append('('+paren+')')
        for x in xrange(1,n):
            for parenL in self.generateParenthesis(x):
                for parenR in self.generateParenthesis(n-x):
                    parens.append(parenL+parenR)
        return list(set(parens))
