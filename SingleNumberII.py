class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one,two = 0,0
        for i in A:
            one = (one^i)&(~two)
            two = (two^i)&(~one)
        return one
