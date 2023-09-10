# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? 
# Our goal is to create a function that will check that for us!
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
          
board = [[0, 0, 1], 
         [0, 1, 2], 
         [2, 1, 0]] 



def is_solved(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]  

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    


            
print (is_solved(board))