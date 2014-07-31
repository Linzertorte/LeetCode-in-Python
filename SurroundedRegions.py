class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        def bfs(i,j,board):
            board[i][j]='P'
            q = collections.deque()
            q.append((i,j))
            while q:
                i,j = q.popleft()
                for dx in xrange(-1,2):
                    for dy in xrange(-1,2):
                        if (dx==0) ^ (dy==0):
                            x,y = i+dx,j+dy
                            if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
                                continue
                            if board[x][y]=='O':
                                board[x][y] = 'P'
                                q.append((x,y))
        
        n = len(board)
        if n==0:
            return
        m = len(board[0])
        for i in xrange(n):
            if board[i][0] =='O':
                bfs(i,0,board)
            if board[i][m-1]=='O':
                bfs(i,m-1,board)
        for i in xrange(m):
            if board[0][i] =='O':
                bfs(0,i,board)
            if board[n-1][i]=='O':
                bfs(n-1,i,board)
        for i in xrange(n):
            for j in xrange(m):
                if board[i][j]=='P':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j] = 'X'
        
