def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-"*9)
    print("/n")

def check_winner(board):
    for row in board:
        if row[0]==row[1]==row[2] !=' ':
            return row[0]

    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]!=' ':
            return board[0][col]

    if board[0][0]==board[1][1]==board[2][2] !=' ':
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] != ' ':
        return board[0][2]

    return None

def is_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board, player):
    while True:
        try:
            move=int(input(f"Player {player}, enter position (1-9): "))-1
            if move<0 or move>8:
                print("Invalid position! Choose between 1 and 9.")
                continue

            row, col=divmod(move, 3)
            if board[row][col]==' ':
                board[row][col]=player
                break
            else:
                print("That cell is already taken. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def main():
    board=[[' ' for _ in range(3)]for _ in range(3)]
    current_player='X'

    print("Welcome to Tic Tac Toe!")
    print("Positiond are numbered like this:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")

    while True:
        print_board(board)
        player_move(board, current_player)

        winner=check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins !")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player='0' if current_player=='X' else 'X'


if __name__=="__main__":
    main()