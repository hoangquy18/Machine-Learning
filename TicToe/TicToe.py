import sys
from tkinter import *
from Board import Board
from Player import Player
from threading import Thread

if __name__ == "__main__":
    board = Board()
    board.inputRowCol()
    root_board = Tk()
    root_board.title("Cờ Caro")
    board.initBoard(root_board)
    player_frame = Frame(root_board)
    player = Player(player_frame,board.button_board,board.board,board.row,board.col)
    while True:
        player.Play()
        root_board.mainloop()


