class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def kth(x,y,k):
            n,m = len(x),len(y)
            if n==0: return y[k-1]
            if m==0: return x[k-1]
            xm,ym=n/2,m/2
            if x[xm]>y[ym]:
                x,y,xm,ym,n,m = y,x,ym,xm,m,n
            if k<=xm+ym+1:
                return kth(x,y[:ym],k)
            else: return kth(x[xm+1:],y,k-xm-1)
        n,m = len(nums1),len(nums2)
        k = (n+m)/2
        if (n+m)%2==1:
            return kth(nums1,nums2,k+1)
        else: return (kth(nums1,nums2,k)+kth(nums1,nums2,k+1))/2.0
