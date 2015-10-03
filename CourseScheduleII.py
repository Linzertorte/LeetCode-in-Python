class Solution(object):
    def findOrder(self, n, prerequisites):
        edge = [[] for i in xrange(n)]
        for p in prerequisites:
            u,v = p
            edge[u].append(v)
        visited = [0]*n
        cnt = [2]
        def conflict(i):
            if visited[i]==1: return True
            if visited[i]>=2: return False
            visited[i] = 1
            for j in edge[i]:
                if conflict(j): return True
            visited[i] = cnt[0]
            cnt[0] += 1
            return False
        for i in xrange(n):
            if visited[i]==0:
                if conflict(i): return []
        return sorted(range(0,n), key=lambda x:visited[x])
