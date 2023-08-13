"""Koorosh Asil , 40124463, Computer science, Sdouku"""
import random
import numpy as np
from tkinter import *
from tkinter import filedialog

class Sudoku:
    
    def __init__(self):
        self.board = [[0 for i in range(9)]for i in range(9)]
        self.window = Tk()
        self.window.geometry("541x655")
        self.window.title("Sudoku")
        
        solbut = Button(self.window, text="solution", bg = "yellow", command= self.show_solutuin)
        solbut.place(x =250, y = 600, width=50, height=30)
        another = Button(self.window, text="another", bg = "yellow", command= self.quitloop)
        another.place(x =310, y = 600, width=50, height=30)
        exitbut = Button(self.window,text="quit", bg = "yellow", command= self.exitcode)
        exitbut.place(x =370, y = 600, width=50, height=30)
        checking = Button(self.window, text="check", bg = "yellow", command= self.show_win)
        checking.place(x =190, y = 600, width=50, height=30)
        generate = Button(self.window, text="generate", bg = "yellow", command= self.generate_soduku)
        generate.place(x =430, y = 600, width=50, height=30)
        loading = Button(self.window, text="load", bg = "yellow", command= self.load_puzzle)
        loading.place(x =120, y = 600, width=50, height=30)
        clearing = Button(self.window, text="clear", bg = "yellow", command= self.clear)
        clearing.place(x =60, y = 600, width=50, height=30)
        self.var = IntVar()
        
        option1 = Radiobutton(self.window, text="easy", variable=self.var, value=1, bg = "gray", font = "Areal 13")
        option2 = Radiobutton(self.window, text="medium", variable=self.var, value=2, bg = "gray",font = "Areal 13")
        option3 = Radiobutton(self.window, text="hard", variable=self.var, value=3, bg = "gray", font = "Areal 13")
        option1.place(x =90, y = 560,width=80, height=20)
        option2.place(x =180, y = 560,width=80, height=20)
        option3.place(x =270, y = 560, width=80, height=20)

    def quitloop(self):
        self.window.quit()
    
    def exitcode(self):
        exit()
    
    def load_puzzle(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as f:
                sudoku = []
                for line in f:
                    row = [int(num) for num in line.strip().split(',')]
                    sudoku.append(row)
        self.board = sudoku
        self.make_gui()
            
    def is_sudoku_grid(self, board):
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False
        for row in range(9):
            for col in range(9):
                if not isinstance(board[row][col], int) and board[row][col] is not None:
                    return False
                if board[row][col] not in [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    return False
        for i in range(9):
            if not self.is_complete_set(board[i]): # if not set(board[i])
                return False
            if not self.is_complete_set([board[j][i] for j in range(9)]):
                return False
            box_row = (i // 3) * 3
            box_col = (i % 3) * 3
            if not self.is_complete_set([board[box_row+j][box_col+k] for j in range(3) for k in range(3)]):
                return False
        return True

    def is_complete_set(self,nums):
        return set(nums) == set(range(1, 10))

    def show_win(self):
        if self.is_sudoku_grid(self.board) :
            label = Label(self.window, bg = "green", text= "you won", font = "Areal 20 bold")
        else:
            label = Label(self.window, bg = "red", text= "you lost", font = "Areal 20 bold")
        label.place(x = 180,y = 240, width=180, height=60 )
    
    def check(self,board,row,col,number) :
        for i in range(9) :
            if board[row][i] == number:
                return False
        for j in range(9) :
            if board[j][col] == number:
                return False
        x = row//3 *3
        y = col//3 *3
        
        for i in range(3):
            for j in range(3):
                if board[x+i][y+j] == number:
                    return False
        else:
            return True
        
    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i,j
        return None
        
    def generate_random_board(self,board):
        house = self.find_empty(board)
        if house is None:  # if find != False
            return True
        else:
            row, col = house
        for number in range(1, 10):
            random_number = random.randint(1, 9)
            if self.check(board, row, col,random_number):
                board[row][col] = random_number
                if self.generate_random_board(board):
                    return True
                board[row][col] = 0
        return False
    
    def delete(self,board, how_many) :
        while how_many :
            x = random.randint(0,8)
            y = random.randint(0,8)
            if board[x][y]!= 0:
                board[x][y] = 0
                how_many = how_many - 1
    
    def solve(self,board):
        for i in range(9) :
            for j in range(9):
                if board[i][j] == 0:
                    for k in range(1,10) :
                        if self.check(board, i, j, k):
                            board[i][j]=k
                            self.solve(board)
                            board[i][j]=0
                    return
        self.make_gui()
        self.window.mainloop()
    
    def generate_soduku(self) :
        self.generate_random_board(self.board)
        self.level = self.var.get()
        if self.level == 1 :
            self.delete(self.board, 30)
        elif self.level == 2 :
            self.delete(self.board, 40)
        elif self.level == 3 :
            self.delete(self.board, 50) 
        self.make_gui()
    
    def make_gui(self):
        cl_houses = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), 
                    (2, 3), (2, 4), (2, 5), 
                    (3, 0), (3, 1),(3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2),
                    (6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5),
                    (3,6),(4,6),(5,6),(3,7),(4,7),(5,7),(3,8),(4,8),(5,8)]
    
        self.window.config(bg= "gray")
        self.entries = [[] for i in range(9)] # needed to set entries 
        
        for a in range(0, 9):
            for b in range(0,9):
                if self.board[b][a] == 0:
                    color  = "blue"
                else:
                    color = "black"
                temp = Entry(self.window,justify=CENTER, bg = "light gray",font = "Areal 20 bold", fg = color)
                if self.board[b][a] != 0 :
                    temp.insert(30,self.board[b][a])
                temp.place(x=a*60, y=b*60, width=60, height=60)
                self.entries[b].append(temp)
                if (a,b) in cl_houses :
                    self.entries[b][a].config(bg="white")
        self.binder(self.entries)
        
    def change(self,sud, entries, i,j):
        var= int(entries[i][j].get())
        entries[i][j].config(bg = "light blue")
        sud[i][j] = var
        
    def binder(self,entries) :
        for a in range(9) :
            for b in range(9) :
                entries[a][b].bind("<Return>", lambda event,t = self.board,e = self.entries, j = b, i = a : self.change(t,e,i,j))
    
    def show_solutuin(self):
        self.solve(self.board)
        
    def clear(self):
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.make_gui()

puz = Sudoku()
puz.make_gui()
puz.window.mainloop()