#1.Find Empty
#2.Check valid solution
#3.Check for completion
#4.Backtracking
sudoku_board = [
    [1,0,0,0,3,0,0,0,9],
    [0,2,0,6,4,0,0,8,0],
    [0,0,3,2,0,0,7,4,0],
    [2,0,0,0,0,0,0,0,0],
    [0,1,4,0,0,0,0,0,0],
    [0,0,0,0,6,2,8,0,0],
    [0,0,7,0,0,0,3,0,0],
    [0,8,0,4,5,0,0,2,0],
    [0,0,0,0,0,0,0,0,1]
]

def print_board(board):
    for y in board:
        for x in y:
            print(str(x) + "\t",end= "")
        print("\n")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
            #row,col


def check_valid(board, val, pos):
    #check row
    for y in range(len(board[0])):
        if board[pos[0]][y] == val and y != pos[1]:
            return False

    #check column
    for x in range(len(board)):
        if board[x][pos[1]] == val and x != pos[0]:
            return False

    #check small box
    box_x=pos[0]//3
    box_y=pos[1]//3

    for y in range(box_y*3,box_y*3 + 3):
        for x in range(box_x*3,box_x*3 + 3):
            if board[x][y] == val and (x,y) != pos:
                return False

    #if all conditions are valid
    return  True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    else:
        row, col = empty

    for i in range(1,10):
        if check_valid(board,i,(row,col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

print_board(sudoku_board)
solve(sudoku_board)
print("\n\n")
print_board(sudoku_board)