import math

# Board
board = [" " for _ in range(9)]

# Print Board
def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Check Winner
def check_winner(b, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False

# Check Draw
def is_draw():
    return " " not in board

# Minimax AI
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if " " not in b:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth+1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth+1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Player Move
def player_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Position already taken!")
        except:
            print("Invalid input!")

# Game Loop
def play():
    print("TIC TAC TOE 🤖")
    print("You = X | AI = O")

    while True:
        print_board()
        player_move()

        if check_winner(board, "X"):
            print_board()
            print("🎉 You Win!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

        ai_move()

        if check_winner(board, "O"):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

# Run Game
play()