class Solution(object):
    def letterCombinations(self, digits):
        letter={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxzy'}
        def dfs(digits):
            if len(digits)==0: return ['']
            return [x+p for p in dfs(digits[1:]) for x in letter[digits[0]]]
        return dfs(digits) if digits else []
