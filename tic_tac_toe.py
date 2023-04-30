
import random

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

game_on = True
default_sign = "-"


def display_board():
    print(board[0] + "|" + board[1] + "|"+ board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|"+ board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|"+ board[8])
def play_game():
    display_board()
    while "-" in board:
        handle_turn()
        
        if(check_win() != None):
            print(check_win())
            break
    check_win()
    check_tie()
        

    
def handle_turn():
    while "-" in board:
        user_input = (int(input("enter number from(1-9): "))-1)
        #user input
        if (board[user_input] == "-"):
            board[user_input] = "X"
            break
        else:
            print("Oops!try again")
            display_board()
       
    #computer_input  
    while "-" in board:  
        computer_input = random.randint(0, 8)
        if(board[computer_input] == "-"):
            board[computer_input] = "O"
            break
        
    display_board()

def check_win():
    #rows
    if(board[0] == board[1] == board[2] != "-"):
        return "winner is "+ board[0] 
    elif(board[3] == board[4] == board[5] != "-"):
        return"winner is "+ board[3]
    elif(board[6] == board[7] == board[8] != "-"):
        return"winner is "+ board[6]
    #columns
    elif(board[0] == board[3] == board[6] != "-"):
        return "winner is "+ board[0]
    elif(board[1] == board[4] == board[7] != "-"):
        return"winner is "+ board[1]
    elif(board[2] == board[5] == board[8] != "-"):
        return"winner is "+ board[2]
    #diagonal
    elif(board[0] == board[4] == board[8] != "-"):
        return "winner is "+ board[0]
    elif(board[2] == board[4] == board[6] != "-"):
        return "winner is "+ board[2]
    else:
        return None
def check_tie():
    if ("-"  not in board )and (check_win() == None):
        print("it is a tie")
play_game()
    