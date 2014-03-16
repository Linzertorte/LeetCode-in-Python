class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        ops={'+':(lambda x,y:x+y),
            '-':(lambda x,y:x-y),
            '*':(lambda x,y:x*y),
            '/':(lambda x,y:x/y if x/y>=0 or x%y==0 else x/y+1)}
        for token in tokens:
            if token in ops:
                a=stack.pop()
                b=stack.pop()
                stack.append(ops[token](b,a))
            else:
                stack.append(int(token))
        return stack.pop()
