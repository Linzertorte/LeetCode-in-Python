class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x<=1:
            return x
        low,high=0,x;
        while low+1<high:
            mid=(low+high)/2
            if(mid*mid<=x):
                low=mid
            else:
                high=mid
        return low
