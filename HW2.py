import numpy as np

def create_board():
    return np.zeros ((3,3))

board = create_board()

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    
board = create_board() 
place(board , 1 , (0,0))

def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))

print(possibilities(board))

import random 
random.seed(1)

def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board

random_place(board, 2)

random.seed(1)
board = create_board()

for i in range(3):
    random_place(board, 1)
    random_place(board, 2)

print(board)

def check_row(row, player):
    for marker in row:
        if marker != player:
            return False
    return True

def row_win(board, player):
    for row in board:
        if check_row(row, player):
            return True
    return False         

row_win(board, 1)


def col_win(board, player):
    for row in board.T:
        if check_row(row, player):
            return True
    return False

col_win(board,1)

board[1,1] = 2

def diag_win(board, player):
    main_diag = board.diagonal()
    anti_diag = np.flipud(board).diagonal()[::-1]
    return check_row(main_diag, player) or check_row(anti_diag, player)

diag_win(board,2)
print(board)

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board, player) or diag_win(board, player) or col_win(board, player):
            return player
    if np.all(board != 0):
        winner = -1
    return winner

evaluate(board)

random.seed(1)

def play_game():
    board = create_board()
    while True:
        for player in [1, 2]:
            random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result
results = []            
for i in range(1000):            
    result = play_game()
    results.append(result)

win_1 = 0
win_2 = 0
tie = 0
for result in results:
    if(result == 1):
        win_1 += 1
    elif(result == 2):
        win_2 += 1
    else:
        tie += 1
        
print(win_1)
print(win_2)
print(tie)

random.seed(1)

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            board = random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner    

results2 = []            
for i in range(1000):            
    result = play_strategic_game()
    results2.append(result)

win_1 = 0
win_2 = 0
tie = 0
for result in results2:
    if(result == 1):
        win_1 += 1
    elif(result == 2):
        win_2 += 1
    else:
        tie += 1
        
print(win_1)
print(win_2)
print(tie)