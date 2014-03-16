class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        """
        find first x that x<target  A[hi]>=target
        """
        if A[-1]<target:
            return len(A)
        if target<=A[0]:
            return 0
        lo,hi=0,len(A)-1
        while lo+1<hi:
            mid=(lo+hi)/2
            if A[mid]<target:
                lo=mid
            else:
                hi=mid
        return hi
