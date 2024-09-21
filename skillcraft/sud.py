# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

# Function to check if a number can be placed at a specific position
def is_valid(board, row, col, num):
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

# Function to solve the Sudoku using backtracking
def solve_sudoku(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # Puzzle solved
    
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Tentatively place the number

            if solve_sudoku(board):
                return True
            
            # If the number leads to a wrong solution, backtrack
            board[row][col] = 0  # Reset the cell

    return False

# Function to find an empty cell (denoted by 0)
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# Sample unsolved Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Run the solver and print the result
if solve_sudoku(board):
    print("Solved Sudoku puzzle:")
    print_board(board)
else:
    print("No solution exists.")
