class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):

        def dfs(i,n,s,yes,path,result):
            if i==n:
                result.append(path[:])
                return
            for j in xrange(i+1,n+1):
                if yes[i][j]:
                    path.append(s[i:j])
                    dfs(j,n,s,yes,path,result)
                    path.pop()


        n = len(s)
        yes = [[0]*(n+1) for i in xrange(n+1)]
        for i in xrange(n):
            yes[i][i] = yes[i][i+1] = 1
        for k in xrange(2,n+1):
            for i in xrange(n):
                j = i+k
                if j>n:
                    continue
                if s[i]==s[j-1] and yes[i+1][j-1]:
                    yes[i][j] = 1
        result = []
        path = []
        dfs(0,n,s,yes,path,result)
        return result
