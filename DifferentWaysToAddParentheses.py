class Solution(object):
    def diffWaysToCompute(self, expr):
        op = {'+': lambda x,y: x+y,
              '-': lambda x,y: x-y,
              '*': lambda x,y: x*y}
        ops = re.split('\d+',expr)[1:-1]
        nums = map(int,re.split('[^\d]',expr))
        def dfs(nums,ops):
            if len(nums)==1: return nums
            return [op[ops[i]](x,y) for i in xrange(len(ops)) for x in dfs(nums[:i+1],ops[:i]) for y in dfs(nums[i+1:],ops[i+1:])]               
        return dfs(nums,ops)
