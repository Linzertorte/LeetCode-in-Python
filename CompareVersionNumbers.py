class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        n,m = len(v1),len(v2)
        for i in xrange(max(n,m)):
            x = int(v1[i]) if i<n else 0
            y = int(v2[i]) if i<m else 0
            if x<y: return -1
            if x>y: return 1
        return 0
