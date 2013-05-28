'''
Created on 27/05/2013

@author: Antek
'''
from Tkinter import *
from board import Board

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        self.board = Board([[0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0]])
        self.text = Text(frame)
        self.text.config(width=10, height = 10)
        self.text.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Evolve", command=self.evolve)
        self.hi_there.pack(side=LEFT)
        self.evolve()

    def evolve(self):
        self.board = self.board.evolve()
        self.text.delete('0.0', '3.3')
        self.text.insert(INSERT, str(self.board))


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()