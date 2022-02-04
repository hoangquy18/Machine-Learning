import sys

class Board:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.board = [[" " for j in range(col)] for i in range(row)]
    def printBoard(self):
        print(end=" ")
        for i in range(self.row):
            print(" ",i,end= "")
        print()
        count = 0
        for i in self.board:
            check = 0
            for j in i:
                if check== 0:
                    print(count,end =" ")
                    check+=1
                    count+=1
                print(f"|{j}", end = " ")
            print("|")
    def getCol(self):
        return self.col
    def getRow(self):
        return self.row
    def updateBoard(self,board):
        self.board = board

class Player():
    def __init__(self,board,symbol,row,col):
        self.board = board
        self.symbol = symbol
        self.row = row
        self.col = col
    def checkInput(self,row,col):
        try:
            test = self.board[row][col]
        except IndexError:
            print("Wrong location")
            return False
        if self.board[row][col] != " ":
            print("Wrong location")
            return False
        return True
    
    def Play(self):
        input_row = input("Nhap dong can danh: ")
        while (not input_row.isnumeric()):
            input_row = input("Nhap lai dong can danh: ")
        input_col = input("Nhap cot can danh: ")
        while (not input_col.isnumeric()):
            input_col = input("Nhap lai cot can danh: ")
        input_row = int(input_row)
        input_col = int(input_col)
        while (not self.checkInput(input_row,input_col)):
            input_row = int(input("Nhap lai dong can danh: "))
            input_col = int(input("Nhap lai cot can danh: "))
        self.board[input_row][input_col] = self.symbol
        return input_row,input_col

    def checkWinConditionUp(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.symbol and input_row <= self.row: #ktra nguoc
                return 1 + self.checkWinConditionUp(input_row+1,input_col)
            return 0
        except IndexError:
            return 0
    def checkWinConditionDown(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.symbol and input_row >= 0:
                return 1 + self.checkWinConditionDown(input_row-1,input_col)
            else:
                return 0
        except IndexError:
            return 0

    def checkWinConditionLeft(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.symbol and input_col<= self.col:
                return 1 + self.checkWinConditionLeft(input_row,input_col+1)
            else:
                return 0
        except IndexError:
            return 0
    def checkWinConditionRight(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.symbol and input_col >= 0:
                return 1 + self.checkWinConditionRight(input_row,input_col-1)
            else:
                return 0
        except IndexError:
            return 0

    def checkWinConditionDiagUpLeft(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.symbol and input_col <= self.col and input_row <= self.row:
                return 1 + self.checkWinConditionDiagUpLeft(input_row+1,input_col+1)
            else:
                return 0
        except IndexError:
            return 0
    def checkWinConditionDiagDownRight(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.symbol and input_col >=0 and input_row >=0:
                return 1 + self.checkWinConditionDiagDownRight(input_row-1,input_col-1)
            else:
                return 0
        except IndexError:
            return 0

    def checkWinConditionDiagUpRight(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.symbol and input_col >=0 and input_row <=self.row:
                return 1 + self.checkWinConditionDiagUpRight(input_row+1,input_col-1)
            else:
                return 0
        except IndexError:
            return 0
    def checkWinConditionDiagDownLeft(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.symbol and input_col <= self.col and input_row >=0:
                return 1 + self.checkWinConditionDiagDownLeft(input_row-1,input_col+1)
            else:
                return 0
        except IndexError:
            return 0

    def VerticalWin(self,input_row,input_col):
        if (self.checkWinConditionUp(input_row+1,input_col) + self.checkWinConditionDown(input_row-1,input_col) + 1) == 5:
            print("end")
            return True
    def HorizonalWin(self,input_row,input_col):
        if (self.checkWinConditionLeft(input_row,input_col+1) + self.checkWinConditionRight(input_row,input_col-1) +1) == 5:
            print("end")
            return True
    def DiagLeftRightWin(self,input_row,input_col):
        if (self.checkWinConditionDiagUpLeft(input_row+1,input_col+1) + self.checkWinConditionDiagDownRight(input_row-1,input_col-1)+1) == 5:
            print("end")
            return True
    def DiagRightLeftWin(self,input_row,input_col):
        if (self.checkWinConditionDiagUpRight(input_row+1,input_col-1) + self.checkWinConditionDiagDownLeft(input_row-1,input_col+1)+1) == 5:
            print("end")
            return True
    
    def updateBoard(self,board):
        self.board = board

input_row = input("Nhap dong cua bang: ")
while (not input_row.isnumeric()):
    input_row = input("Nhap lai dong cua bang: ")
input_col = input("Nhap cot cua bang: ")
while (not input_col.isnumeric()):
    input_col = input("Nhap lai cot cua bang: ")
input_row = int(input_row)
input_col = int(input_col)

board = Board(input_row,input_col)
player1 = Player(board.board,'X',board.getRow(),board.getCol())
player2 = Player(board.board,'O',board.getRow(),board.getCol())
board.printBoard()
while True:
    print("Player 1 play: ")
    input_row_1,input_col_1 = player1.Play()
    player2.updateBoard(player1.board)
    board.updateBoard(player2.board)
    if player1.DiagRightLeftWin(input_row_1,input_col_1) or player1.VerticalWin(input_row_1,input_col_1) or player1.HorizonalWin(input_row_1,input_col_1) or player1.DiagLeftRightWin(input_row_1,input_col_1):
        board.printBoard()
        print("Player 1 Win")
        sys.exit()
    board.printBoard()
    print("Player 2 play: ")
    input_row_2,input_col_2= player2.Play()
    player1.updateBoard(player2.board)
    board.updateBoard(player1.board)
    if player2.DiagRightLeftWin(input_row_2,input_col_2) or player2.VerticalWin(input_row_2,input_col_2) or player2.HorizonalWin(input_row_2,input_col_2) or player2.DiagLeftRightWin(input_row_2,input_col_2):
        board.printBoard()
        print("Player 2 Win")
        sys.exit()
    board.printBoard()
