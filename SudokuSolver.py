class Solution(object):
    def solveSudoku(self, board):
        print board
        col,row,box=[set() for i in xrange(9)],[set() for i in xrange(9)],[set() for i in xrange(9)]
        def box_id(i,j):
            return (i/3)*3 + j/3
        def can_place(i,j,x):
            return (x not in row[i]) and (x not in col[j]) and (x not in box[box_id(i,j)])
        def place(i,j,x):
            row[i].add(x)
            col[j].add(x)
            box[box_id(i,j)].add(x)
        def remove(i,j,x):
            row[i].remove(x)
            col[j].remove(x)
            box[box_id(i,j)].remove(x)
        
        for i in xrange(0,9):
            for j in xrange(0,9):
                if board[i][j]!='.':
                    place(i,j,board[i][j])
        def dfs(i,j):
            print '(',i,j,')'
            if i==9: return True
            if j==9: return dfs(i+1,0)
            if board[i][j]!='.': return dfs(i,j+1)
            for x in xrange(1,10):
                x = str(x)
                if can_place(i,j,x):
                    board[i][j]=x
                    place(i,j,x)
                    if dfs(i,j+1):
                        return True
                    board[i][j]='.'
                    remove(i,j,x)
            return False
        dfs(0,0)
