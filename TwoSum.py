class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        V={}
        for i,n in enumerate(num):
            if target-n in V:
                return (V[target-n],i+1)
            else:
                V[n]=i+1
