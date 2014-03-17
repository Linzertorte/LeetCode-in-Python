class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i,j=-1,-1
        for k in xrange(len(A)):
            if A[k]==1:
                j+=1
                A[j],A[k]=A[k],A[j]
            elif A[k]==0:
                j+=1
                A[j],A[k]=A[k],A[j]
                i+=1
                A[i],A[j]=A[j],A[i]
