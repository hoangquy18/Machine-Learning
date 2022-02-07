from tkinter import messagebox
import sys

class Player():
    def __init__(self,root_board,button_board,board,row,col):
        self.board = board
        self.row = row
        self.col = col
        self.button_board = button_board
        self.root_board = root_board
        self.turn = 'X'
    def checkInput(self,row,col):
        if self.board[row][col] != " ":
            messagebox.askretrycancel("Thử lại", "Vui lòng chọn vị trí khác")
            return False
        return True
    def change(self,i,j):
        # self.checkInput(i,j)
        if not self.checkInput(i,j):
            return
        if self.turn == 'X':
            self.button_board[i][j]['text'] = self.turn
            self.board[i][j] = self.turn
            if self.DiagRightLeftWin(i,j) or self.VerticalWin(i,j) or self.HorizonalWin(i,j) or self.DiagLeftRightWin(i,j):
                messagebox.showinfo("Kết thúc", "X thắng")
                sys.exit()
            self.turn = 'O'
        else:
            self.button_board[i][j]['text'] = self.turn
            self.board[i][j] = self.turn
            if self.DiagRightLeftWin(i,j) or self.VerticalWin(i,j) or self.HorizonalWin(i,j) or self.DiagLeftRightWin(i,j):
                messagebox.showinfo("Kết thúc", "O thắng")
                sys.exit()
            self.turn = 'X'
    def Play(self): #trigger
        for i in range(self.row):
            for j in range(self.col):
                self.button_board[i][j].configure(command = lambda _i = i,_j = j: self.change(_i,_j))

    def updateBoard(self,board):
        self.board = board
    def updateButtonBoard(self,button_board):
        self.button_board = button_board

    def checkWinConditionUp(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.turn and input_row <= self.row: #ktra nguoc
                return 1 + self.checkWinConditionUp(input_row+1,input_col)
            return 0
        except IndexError:
            return 0
    def checkWinConditionDown(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.turn and input_row >= 0:
                return 1 + self.checkWinConditionDown(input_row-1,input_col)
            else:
                return 0
        except IndexError:
            return 0

    def checkWinConditionLeft(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.turn and input_col<= self.col:
                return 1 + self.checkWinConditionLeft(input_row,input_col+1)
            else:
                return 0
        except IndexError:
            return 0
    def checkWinConditionRight(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.turn and input_col >= 0:
                return 1 + self.checkWinConditionRight(input_row,input_col-1)
            else:
                return 0
        except IndexError:
            return 0

    def checkWinConditionDiagUpLeft(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.turn and input_col <= self.col and input_row <= self.row:
                return 1 + self.checkWinConditionDiagUpLeft(input_row+1,input_col+1)
            else:
                return 0
        except IndexError:
            return 0
    def checkWinConditionDiagDownRight(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.turn and input_col >=0 and input_row >=0:
                return 1 + self.checkWinConditionDiagDownRight(input_row-1,input_col-1)
            else:
                return 0
        except IndexError:
            return 0

    def checkWinConditionDiagUpRight(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.turn and input_col >=0 and input_row <=self.row:
                return 1 + self.checkWinConditionDiagUpRight(input_row+1,input_col-1)
            else:
                return 0
        except IndexError:
            return 0
    def checkWinConditionDiagDownLeft(self,input_row,input_col):
        try:
            if self.board[input_row][input_col] == self.turn and input_col <= self.col and input_row >=0:
                return 1 + self.checkWinConditionDiagDownLeft(input_row-1,input_col+1)
            else:
                return 0
        except IndexError:
            return 0

    def VerticalWin(self,input_row,input_col):
        if (self.checkWinConditionUp(input_row+1,input_col) + self.checkWinConditionDown(input_row-1,input_col) + 1) == 5:
            return True
    def HorizonalWin(self,input_row,input_col):
        if (self.checkWinConditionLeft(input_row,input_col+1) + self.checkWinConditionRight(input_row,input_col-1) +1) == 5:
            return True
    def DiagLeftRightWin(self,input_row,input_col):
        if (self.checkWinConditionDiagUpLeft(input_row+1,input_col+1) + self.checkWinConditionDiagDownRight(input_row-1,input_col-1)+1) == 5:
            return True
    def DiagRightLeftWin(self,input_row,input_col):
        if (self.checkWinConditionDiagUpRight(input_row+1,input_col-1) + self.checkWinConditionDiagDownLeft(input_row-1,input_col+1)+1) == 5:
            return True
