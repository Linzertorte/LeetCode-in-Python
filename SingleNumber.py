class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        single = 0
        for n in A:
            single ^=n
        return single
