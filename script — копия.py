def print_board(board):
    print("  1  2  3")
    for i in range(3):
        print(f"{i+1}  {' '.join(board[i])} ")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        col = int(input("Выберите столбец: ")) - 1
        if col < 0 or col > 2:
            print("Введите число от 1 до 3")
            continue
        row = int(input("Выберите строку: ")) - 1
        if row < 0 or row > 2:
            print("Введите число от 1 до 3")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Игрок {player} победил!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("Эта клетка уже занята. Попробуйте снова.")

tic_tac_toe()