# Check if placing a queen at board[row][col] is safe
def is_safe(board, row, col):
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal (left)
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal (left)
    i, j = row, col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


# Solve using Backtracking
def solve_8_queens(board, col):
    # All queens placed
    if col >= 8:
        return True

    # Try each row in the current column
    for row in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen

            if solve_8_queens(board, col + 1):
                return True

            board[row][col] = 0  # Backtrack

    return False


# Begin solving
board = [[0 for _ in range(8)] for _ in range(8)]

if solve_8_queens(board, 0):
    print("\n8 Queens Solution:\n")
    for row in board:
        print(row)
else:
    print("No solution found.")

