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

def new_entry(board):
    new_board = str(input("Enter a 9x9 sudoku board in a linear sequential manner or type 0 for test case.\n"))
    if len(new_board) < 81:
        print("Using default values.")
        return False
    else:
        index = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=int(new_board[index])
                index+=1


def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i!=0:
            print("-----------------------------------------")
        for j in range(len(board[0])):
            if j%3 == 0 and j!=0:
                print("|\t",end="")
            if board[i][j] != 0:
                cell = board[i][j]
            else:
                cell = "_"
            print(str(cell) + "\t", end="")
        print("\n",end="")


def empty_block(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return i,j


def valid(board,val,pos):
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i]==val and i!=pos[1]:
            return False

    #check column
    for j in range(len(board)):
        if board[j][pos[1]]==val and j!=pos[0]:
            return False

    #check small box
    box_x=pos[1]//3
    box_y=pos[0]//3
    for i in range(box_x*3,box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if board[j][i]==val and (i,j) != pos:
                return False

    return True


def solve(board):
    blank=empty_block(board)
    if not blank:
        return True
    else:
        row, col = blank
        for i in range(1,10):
            if valid(board,i,(row,col)):
                board[row][col]=i
                if solve(board):
                   return True

                board[row][col]=0

    return False


def main():
    new_entry(sudoku_board)
    print("Problem: ")
    print_board(sudoku_board)
    solve(sudoku_board)
    print("\n\nSolution: ")
    print_board(sudoku_board)


main()
