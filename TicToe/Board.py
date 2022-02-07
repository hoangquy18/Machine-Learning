from email import message
from tkinter import *
from tkinter import messagebox

class Board():
    def __init__(self,row=0,col=0):
        self.row = row
        self.col = col
        self.board = None
        self.button_board = None
        self.phase = 0
        self.check = 0
    def destroy_and_getColRow(self,input_board,entry_row,entry_col):
        if self.check != 2:
            messagebox.showwarning("Cảnh báo","Vui lòng nhập đầy đủ và kiểm tra")
            return
        self.row,self.col = entry_row.get(),entry_col.get()
        self.phase = 1
        input_board.destroy()
    def checkInput(self,text,button_check):
        if text.isnumeric():
            self.check += 1
            messagebox.showinfo("Hoàn tất","Nhập thành công")
            button_check.grid_forget()
        else:
            messagebox.showinfo("Thử lại","Vui lòng nhập số")
    def inputRowCol(self):
        input_board = Tk() 
        label_row = Label(input_board,text = 'Nhập số dòng')
        entry_row = Entry(input_board)
        global button_check_row,button_check_col
        button_check_row = Button(input_board,text= 'Kiểm tra',command = lambda : self.checkInput(entry_row.get(),button_check_row))
        button_check_row.grid(row = 0,column=2)

        label_row.grid(row=0,column=0)
        entry_row.grid(row = 0,column = 1)

        label_col = Label(input_board,text = 'Nhập số cột')
        entry_col = Entry(input_board)
        button_check_col = Button(input_board,text= 'Kiểm tra',command = lambda : self.checkInput(entry_col.get(),button_check_col))
        button_check_col.grid(row = 1,column=2)
        label_col.grid(row=1,column=0)
        entry_col.grid(row=1,column=1)

        destroy_button = Button(input_board,text = "Đã nhập xong!",command = lambda : self.destroy_and_getColRow(input_board,entry_row,entry_col))
        destroy_button.grid(row = 3,column = 2)

        input_board.mainloop()


    def initBoard(self,root_board):
        button_board = []
        self.row,self.col = int(self.row),int(self.col)
        self.root_board = root_board
        for i in range(self.row):
            line = []
            for j in range(self.col):
                button = Button(self.root_board,text = " ",height = 3,width=10)
                button.grid(row =i,column=j)
                line.append(button)
            button_board.append(line)
        self.button_board = button_board


        board = []
        for i in button_board:
            line = []
            for j in i:
                line.append(j['text'])
            board.append(line)
        self.board = board
        while (self.phase ==0 ): pass

    def getCol(self):
        return self.col
    def getRow(self):
        return self.row
    def updateBoard(self,board):
        self.board = board
    def updateButtonBoard(self,button_board):
        self.button_board = button_board


