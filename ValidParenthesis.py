class Solution:
    # @return a boolean
    def isValid(self, s):
        pa={'(':')','{':'}','[':']'}
        stack=[]
        for p in s:
            if p in pa:
                stack.append(p)
            else:
                if len(stack)==0 or\
                pa[stack.pop()]!=p:
                    return False
        return len(stack)==0
