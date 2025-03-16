import numpy as np

def knight_tour (n):
    board=[[-1 for i in range (n)] for j in range (n)]
    knight_tour_helper(n=n,board=board, x=0,y=0,count=0)
    print (np.array(board))

    
def knight_tour_helper(n,board,x,y,count):
    if count ==n*n:
        return true
    if ((x<0) or (x>=n) or (y<0) or (y>= n) or board[y][x]!=-1):
        return false
    board [y][x]=count
    for x_move,y_move in zip[-2,-2,-1,-1,1,1,2,2], [-1,1,-2,2,-2,2,-1,1]:
        if  knight_tour_helper(n, loard, x+x_move,y+y_move,count+1):
            return true
    board[y][x]=-1
    return false
knight_tour(7)
