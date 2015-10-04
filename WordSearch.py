class Solution(object):
    def exist(self, board, word):
        dx, dy =[0,0,1,-1], [1,-1,0,0]
        n = len(board)
        if n==0: return word==''
        m = len(board[0])
        n,m = n+2,m+2
        board = [['.']*m] +[['.']+p+['.'] for p in board] + [['.']*m]
        def dfs(i,j,w):
            if not w: return True
            c = board[i][j]
            if board[i][j]!=w[0]: return False
            board[i][j] = '.'
            for k in xrange(0,4):
                if dfs(i+dx[k],j+dy[k],w[1:]): return True
            board[i][j] = c
            return False
        for i in xrange(1,n-1):
            for j in xrange(1,m-1):
                if dfs(i,j,word): return True
        return False
