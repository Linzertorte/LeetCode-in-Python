class Solution:

    def solveSudoku(self, board):

        def no_conflict(r,c,board):
            at = board[r][c]
            for k in xrange(9):
                if k!=c and board[r][k]==at:
                    return False
            for k in xrange(9):
                if k!=r and board[k][c]==at:
                    return False
            box_r = (r/3)*3
            box_c = (c/3)*3
            for i in xrange(box_r,box_r+3):
                for j in xrange(box_c,box_c+3):
                    if (i!=r or j!=c) and board[i][j]==at:
                        return False
            return True

        def dfs(r,c,board):
            if r==9:
                return True
            if c==9:
                return dfs(r+1,0,board)
            if board[r][c]!='.':
                if dfs(r,c+1,board):
                    return True
            else:
                for k in xrange(1,10):
                    board[r][c]=str(k)
                    if no_conflict(r,c,board) and dfs(r,c+1,board):
                        return True
                    board[r][c]='.'
            return False

        dfs(0,0,board)
