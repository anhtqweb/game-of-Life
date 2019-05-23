import random

def deadState(width, height):
    board = []
    for i in range(width):
        a = [0] * height
        board.append(a)
    return board

def randomState(width, height):
    board = deadState(width, height)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if random.random() >= 0.5:
                board[row][col] = 1
    return board

def render(board):
    for row in range(len(board)):
        print("|", end = '')
        for col in range(len(board[row])):
            if board[row][col] == 1:
                print("#", end = '')
            else:
                print(" ", end = '')
        print("|")

def neighborCount(board, row, col):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if row + i >= 0 and row + i < len(board) and col + j >= 0 and col + j < len(board[0]):
                count += board[(row+i)][(col+j)]
    return count

def nextState(board):
    newState = deadState(len(board), len(board[0]))
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                count = neighborCount(board, row, col) - 1
                if count == 0 or count == 1:
                    newState[row][col] = 0
                elif count == 2 or count == 3:
                    newState[row][col] = 1
                elif count > 3:
                    newState[row][col] = 0
            else:
                if neighborCount(board, row, col) == 3:
                    newState[row][col] = 1
    return newState

def loadBoard(boardFile):
    fin = open(boardFile, "r")
    board = []
    for line in fin:
        a = []
        for ch in line[:-1]:
            a.append(int(ch))
        board.append(a)
    fin.close()
    return board

def main():
    # init = [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]
    init = loadBoard("f.txt")
    nextBoard = nextState(init)
    while True:
        nextBoard = nextState(nextBoard)
        render(nextBoard)

main()