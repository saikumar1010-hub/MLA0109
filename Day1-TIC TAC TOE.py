def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    # Rows, Columns, Diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, enter your move (row and column 1-3):")

        try:
            row = int(input("Row: ")) - 1
            col = int(input("Column: ")) - 1
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid move! Position out of range.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken!")
            continue

        # Make move
        board[row][col] = current_player

        # Check win
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # Check draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run game
tic_tac_toe()
