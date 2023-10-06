# Tic Tac Toe game
import random
import time

board = ["\n", "1", "2", "3", "\n", "4", "5", "6", "\n", "7", "8", "9"]
def start(board):
    print("Welcome to tic tac toe")
    print("I will go first")
    computerGo(board)


def computerGo(board):
    compNum = random.randint(1, 9)
    if str(compNum) in board:
        indexComp = board.index(str(compNum))
        board[indexComp] = "X"
        print(*board)
        checkerP(board)
    else:
        computerGo(board)
    
def playerGo(board):
    print("Your go!")
    playerNum = input("Pick a place: ")
    if str(playerNum) in board:
        indexComp = board.index(str(playerNum))
        board[indexComp] = "O"
        print(*board)
        checkerC(board)
    
    else:
        print("That number is taken, pick another!")
        playerGo(board)


def checkerC(board):
    if board[1] == "O" and board[2] == "O" and board[3] == "O" or board[5] == "O" and board[6] == "O" and board[7] == "O" or board[9] == "O" and board[10] == "O" and board[11] == "O" or board[1] == "O" and board[5] == "O" and board[9] == "O" or board[2] == "O" and board[6] == "O" and board[10] == "O" or board[3] == "O" and board[7] == "O" and board[11] == "O" or board[1] == "O" and board[6] == "O" and board[11] == "O" or board[7] == "O" and board[6] == "O" and board[3] == "O" or board[9] == "O" and board[6] == "O" and board[3] == "O":
        print("O Wins")
    elif board[1] == "X" and board[2] == "X" and board[3] == "X" or board[5] == "X" and board[6] == "X" and board[7] == "X" or board[9] == "X" and board[10] == "X" and board[11] == "X" or board[1] == "X" and board[5] == "X" and board[9] == "X" or board[2] == "X" and board[6] == "X" and board[10] == "X" or board[3] == "X" and board[7] == "X" and board[11] == "X" or board[1] == "X" and board[6] == "X" and board[11] == "X" or board[7] == "X" and board[6] == "X" and board[3] == "X" or board[9] == "X" and board[6] == "X" and board[3] == "X":
        print("X Wins")
    else:
        print("\n My go!")
        time.sleep(2)
        computerGo(board)

def checkerP(board):
    if board[1] == "O" and board[2] == "O" and board[3] == "O" or board[5] == "O" and board[6] == "O" and board[7] == "O" or board[9] == "O" and board[10] == "O" and board[11] == "O" or board[1] == "O" and board[5] == "O" and board[9] == "O" or board[2] == "O" and board[6] == "O" and board[10] == "O" or board[3] == "O" and board[7] == "O" and board[11] == "O" or board[1] == "O" and board[6] == "O" and board[11] == "O" or board[7] == "O" and board[6] == "O" and board[3] == "O" or board[9] == "O" and board[6] == "O" and board[3] == "O":
        print("\n O Wins")
    elif board[1] == "X" and board[2] == "X" and board[3] == "X" or board[5] == "X" and board[6] == "X" and board[7] == "X" or board[9] == "X" and board[10] == "X" and board[11] == "X" or board[1] == "X" and board[5] == "X" and board[9] == "X" or board[2] == "X" and board[6] == "X" and board[10] == "X" or board[3] == "X" and board[7] == "X" and board[11] == "X" or board[1] == "X" and board[6] == "X" and board[11] == "X" or board[7] == "X" and board[6] == "X" and board[3] == "X" or board[9] == "X" and board[6] == "X" and board[3] == "X":
        print("\n X Wins")
    else:
        playerGo(board)

start(board)

