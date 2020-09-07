#Importing package
import random

#Function to display the board
def display_board(board):
    count=1
    for elements in board:
        #Prints every 3 elements in a row
        print(elements,end="\t")
        if count%3==0:
            print("")
        count=count+1

#Function to input the players marker
def player_input():
    choice = 'wrong'
    while choice not in ['X', 'O']:
        #Takes in the X or O
        choice = input("What would you like to input? X or O ")
        if choice not in ['X', 'O']:
            print("Please make sure to choose X or O.")
    return choice

#Places the marker on the board
def place_marker(board, marker, position):
    board[position]=marker #Assignment

#Checks if the game is won
def win_check(board):
    #Defining the winning patterns
    row1=[board[0],board[1],board[2]]
    row2=[board[3],board[4],board[5]]
    row3=[board[6],board[7],board[8]]
    col1=[board[0],board[3],board[6]]
    col2=[board[1],board[4],board[7]]
    col3=[board[2],board[5],board[8]]
    diag1=[board[0],board[4],board[8]]
    diag2=[board[2],board[4],board[6]]
    Os=["O","O","O"]
    Xs=["X","X","X"]
    #Checking if the pattern has been acheived
    if (row1 == Os) or (row1 == Xs):
        return True
    elif (row2 == Os) or (row2 == Xs):
        return True
    elif (row3 == Os) or (row3 == Xs):
        return True
    elif (col1 == Os) or (col1 == Xs):
        return True
    elif (col2 == Os) or (col2 == Xs):
        return True
    elif (col3 == Os) or (col3 == Xs):
        return True
    elif (diag1 == Os) or (diag1 == Xs):
        return True
    elif (diag2 == Os) or (diag2 == Xs):
        return True
    else:
        return False

#Function to choose a random player to go first
def choose_first():
    #Alternates randomly between 1 and 2
    first=random.randint(1,2)
    if first==1:
        print("Player 1 goes first")
        return 1
    else:
        print("Player 2 goes first")
        return 2

#Checks if there is space in the board
def space_check(board, position):
    if board[position]==" ":
        return True
    else:
        return False

#Checks if the board is full
def full_board_check(board):
    if " " not in board:
        return True
    else:
        return False

#Function to take in a position and check if its valid
def player_choice(board):
    choice = 'wrong'
    flag=False
    while (choice not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) or (flag==False):
        #Takes in a value between 1-9
        choice = input("Pick a position inbetween 1-9: ")
        if choice not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Sorry, but you did not choose a valid position inbetween 1-9")
            continue
        #Checks if there is space
        if space_check(board, int(choice)-1)==False:
                print("That position is occupied, re-enter a new position")
        else:
            flag=True
    return int(choice)-1

#Function to determine replaying
def replay():
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        #Takes in Y or N
        choice = input("Would you like to keep playing? Y or N ")
        if choice not in ['Y', 'N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
    if choice == "Y":
        return True
    else:
        return False

#Driver Program
print('Welcome to Tic Tac Toe!')
while True:
    #Declerations for alternating between X and O
    first=""
    second=""
    temp=""
    flag = True
    #Other general declerations for the game to run
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    choose_first()
    game = True
    #Game running
    while game:
        #Checking if first turn
        if flag:
            marker = player_input()
            flag=False
            if marker == "X":
                first="O"
                second="X"
            else:
                first = "X"
                second = "O"
        #Alternating the marker for each turn
        temp=first
        first=second
        second=temp
        #Assining the marker and displaying
        position = player_choice(board)
        place_marker(board, first, position)
        display_board(board)
        #Check status of game
        if win_check(board)==True:
            print("\nGame Won! Congrats!")
            game=False
        else:
            if full_board_check(board):
                print("Game over! Draw!")
                game=False
    #Check if player wants to replay
    if not replay():
        break
    else:
        flag=True
print("Game over! hope you enjoyed!")