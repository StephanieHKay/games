import random

#create board display
def display_board(board):
    print("\n"*100)
    print(board[6],"|", board[7],"|", board[8])
    print("- - - - -")
    print(board[3], "|", board[4],"|", board[5])
    print("- - - - -")
    print(board[0],"|", board[1],"|", board[2])

#player picks a marker
def player_input():
    player1_marker = "Undecided"
    while player1_marker not in ["X", "O"]:
        player1_marker = input("Player 1, please select a marker, X or O? ")
        if player1_marker not in ["X", "O"]:
            print("Invalid response")

    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"
    return (player1_marker, player2_marker)

#function to place marker on board
def place_marker(board,marker, position):
    board[position] = marker
    return board


#check if a player has won
def win_check(board, mark):
    return (board[6] == board[7] == board[8] == mark) or (board[3] == board[4] == board[5] == mark) or (
                board[0] == board[1] == board[2] == mark) or (board[6] == board[3] == board[0] == mark) or (
                board[7] == board[4] == board[1] == mark) or (board[8] == board[5] == board[2] == mark) or (
                board[6] == board[4] == board[2] == mark) or (board[8] == board[4] == board[0] == mark)

#pick which player to go first
def choose_first():
    random_choice = random.randint(1,2)
    print('Player {} randomly chosen to go first'.format(random_choice))
    return random_choice

#check if any empty spaces on the board
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

#check of all board spaces have been played
def full_board_check(board):
    for item in board:
        if item == " ":
            return False
           
    return True

#play a board position
def player_choice(board):
    choice = 'wrong'
    while choice not in [str(num) for num in range(1, 10)]:
        choice = input('Player please pick a board position from 1-9: ')
        if choice not in [str(num) for num in range(1, 10)]:
            print("Invalid entry")
    position = (int(choice) - 1)
    return position

  
#replay game question
def replay():
    answer = "invalid"
    while answer.upper() not in ["Y", "N"]:
        answer = input("Play again? Y/N ")
        if answer.upper() not in ["Y", "N"]:
            print("That is an invalid response")
    return answer.upper() == "Y"




#game logic
playing_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(playing_board)
print("Welcome to Tic Tac Toe!")


Game = True

while Game == True:

    player1, player2 = player_input()
    if choose_first() ==1:
        player_1_position = player_choice(playing_board)
        while not space_check(playing_board, player_1_position):
            player_1_position = player_choice(playing_board)
        place_marker(playing_board, player1, player_1_position)
        display_board(playing_board)
        player_2_position = player_choice(playing_board)
        while not space_check(playing_board, player_2_position):
            player_2_position = player_choice(playing_board)
        place_marker(playing_board, player2, player_2_position)
        display_board(playing_board)
    else:
        player_2_position = player_choice(playing_board)
        while not space_check(playing_board, player_2_position):
            player_2_position = player_choice(playing_board)
        place_marker(playing_board, player2, player_2_position)
        display_board(playing_board)

    while not win_check(playing_board, "X") and not win_check(playing_board, "O") and not full_board_check(playing_board):
        player_1_position = player_choice(playing_board)
        while not space_check(playing_board, player_1_position):
            player_1_position = player_choice(playing_board)
        place_marker(playing_board, player1, player_1_position)
        display_board(playing_board)
        if win_check(playing_board, "X"):
            print('X has won!')
            if player2 == "X":
                print("Well done player 2")
            else:
                print("Well done player 1")
            Game = False
            break

        elif win_check(playing_board, "0"):
            print('O has won!')
            if player2 == "O":
                print("Well done player 2")
            else:
                print("Well done player 1")
            Game = False
            break
        elif full_board_check(playing_board):
            print('Game is a tie!')
            Game = False
            break

        player_2_position = player_choice(playing_board)
        while not space_check(playing_board, player_2_position):
            player_2_position = player_choice(playing_board)
        place_marker(playing_board, player2, player_2_position)
        display_board(playing_board)
        if win_check(playing_board, "X"):
            print('X has won!')
            if player2 == "X":
                print("Well done player 2")
            else:
                print("Well done player 1")
            Game = False
            break
        elif win_check(playing_board, "O"):
            print('O has won!')
            if player2 == "O":
                print("Well done player 2")
            else:
                print("Well done player 1")
            Game = False
            break
        elif full_board_check(playing_board):
            print('Game is a tie!')
            Game = False
            break

    if replay():
        Game = True
        playing_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        display_board(playing_board)
        print("Welcome to Tic Tac Toe!")
    else:
        Game = False
        print("End of game, see you next time")
