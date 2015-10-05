class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1): return 1
        l,r = 1,n
        while l+1<r:
            mid =(l+r)/2
            if isBadVersion(mid): r=mid
            else: l=mid
        return r
