import math


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} , {board[i+1]} , {board[i+2]}")
        


def isGameOver(board):
    combinations = [(1,2,3),(4,5,6),(7,8,9),
                      (1,4,7),(2,5,8),(3,6,9),
                      (1,5,9),(3,5,7)]
    
    for combs in combinations:
        if board[combs[0]-1] == board[combs[1]-1] == board[combs[2]-1] != " ":
            return board[combs[0]-1]
        
    if " " not in board:
        return "draw"
    
    return None


def evaluate(board):

    winner = isGameOver(board)
    
    if winner == Player_O:
        return 10
    elif winner == Player_X:
        return -10
    else:
        return 0


def get_best_move(board,depth,alpha,beta,is_max):

    if isGameOver(board) is not None or depth == 0:
        return evaluate(board)
    
    if is_max:
        max_val = -math.inf
        for i in range (9):
            if board [i] == " ":
                board [i] = Player_O
                score = get_best_move(board,depth-1,alpha,beta,False)
                board [i] = " "
                max_val = max(max_val,score)
                alpha = max(alpha,score)
                if alpha >= beta:
                    break
        return max_val
    

    else:
        min_val = math.inf
        for i in range (9):
            if board [i] == " ":
                board [i] = Player_X
                score = get_best_move(board,depth-1,alpha,beta,True)
                board [i] = " "
                min_val = min(score,min_val)
                beta = min(beta,score)
                if alpha >= beta:
                    break
        return min_val

def get_comp_move(board):
    best_score = -math.inf
    move = -10
    
    for i in range(9):
        if board[i] == " ":
            board[i] = Player_O
            move_score = get_best_move(board, 9, -math.inf, math.inf, False)
            board[i] = " "
            
            if move_score > best_score:
                best_score = move_score
                move = i
    
    return move

if __name__ == "__main__":
    Player_X = "X"
    Player_O = "O"
    k = 0
    while True:
        print_board(board)
        print('____________')
        winner = isGameOver(board)
        
        if winner is not None:
            if winner == "draw":
                print("It's a draw!")
            else:
                print("Player", winner, "wins!")
            break
        
        if k == 0:
            # Player X's turn (User)
            while True:
                move = int(input("Enter move 1-9: "))
                if board[move-1] == " ":
                    k = 1
                    board[move-1] = Player_X
                    break
                else:
                    print("Invalid move! Try again.")
        else:
            # Player O's turn (AI)
            k = 0
            move = get_comp_move(board)
            board[move] = Player_O