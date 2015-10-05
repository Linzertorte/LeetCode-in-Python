class Solution(object):
    def calculate(self, s):
        s = ''.join([c for c in s if c!=' '])
        def evaluate(s):
            expr = re.split('\+|-',s)
            op = [c for c in s if c=='+' or c=='-']
            if op:
                x = evaluate(expr[0])
                for i in xrange(0,len(op)):
                    x = x+evaluate(expr[i+1]) if op[i]=='+' else x - evaluate(expr[i+1])
                return x
            expr = re.split('\*|\/',s)
            op = [c for c in s if c=='*' or c=='/']
            if op:
                x = evaluate(expr[0])
                for i in xrange(0,len(op)):
                    x = x*evaluate(expr[i+1]) if op[i]=='*' else x / evaluate(expr[i+1])
                return x
            return int(s)
        return evaluate(s)
