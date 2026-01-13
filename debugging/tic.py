def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))  # s'adapte à la taille du plateau

def check_winner(board):
    size = len(board)
    # Lignes
    for row in board:
        if row.count(row[0]) == size and row[0] != " ":
            return row[0]
    # Colonnes
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if column.count(column[0]) == size and column[0] != " ":
            return column[0]
    # Diagonales
    if all(board[i][i] == board[0][0] != " " for i in range(size)):
        return board[0][0]
    if all(board[i][size-1-i] == board[0][size-1] != " " for i in range(size)):
        return board[0][size-1]
    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    max_moves = len(board) * len(board[0])

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0-2) for player {player}: "))
            col = int(input(f"Enter column (0-2) for player {player}: "))
        except ValueError:
            print("Please enter a valid number (0, 1, or 2).")
            continue

        if row not in range(3) or col not in range(3):
            print("Row and column must be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        moves += 1

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if moves == max_moves:
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
