class Solution(object):
    def findWords(self, board, words):
        trie = {'end':False}
        dx, dy =[0,0,1,-1], [1,-1,0,0]
        n = len(board)
        if n==0: return []
        m = len(board[0])
        n,m = n+2,m+2
        board = [['.']*m] +[['.']+p+['.'] for p in board] + [['.']*m]
        def addWords(w):
            p = trie
            for c in w:
                if c not in p: p[c] = {'end':False}
                p = p[c]
            p['end'] = True
        for w in words: addWords(w)
        found = set()
        def dfs(i,j,p,w): #p point to a node in trie, w acc
            c = board[i][j]
            if c=='.': return
            if c not in p:
                return
            p = p[c]
            w+=c
            if p['end']: found.add(w)
            board[i][j] = '.'
            for k in xrange(0,4):
                dfs(i+dx[k],j+dy[k],p,w)
            board[i][j] = c

        for i in xrange(1,n-1):
            for j in xrange(1,m-1):
                dfs(i,j,trie,'')
        return list(found)
