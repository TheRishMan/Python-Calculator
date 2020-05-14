#!/usr/bin/python

from tkinter import *

class Calculator:

    #Adding new character to display
    def action(self,num):
        self.display.config(state = 'normal')
        self.display.insert(END, num)
        self.display.config(state = "disabled")

    #Calculating result
    def calculate(self):
        self.display.config(state = "normal")
        try:
            self.expression = self.display.get(1.0, END)
            self.total = eval(self.expression)
            self.display.delete(1.0,END)
            self.display.insert(END, self.total)
        except SyntaxError or NameError:
            self.display.delete(1.0, END)
            self.display.insert(END, "Error")
        self.display.config(state = "disabled")
        

    #Clearing display
    def clear(self):
        self.display.config(state = "normal")
        self.display.delete(1.0, END)
        self.display.config(state = "disabled")

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg = "light grey")

        #Box where the numbers are typed
        self.display = Text(master, width = 50, height = 5, foreground = "black", background = "white", state = "disabled")

        #Placing that box
        self.display.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

        #Creating buttons
        Button(master, text = "1", width = 11, command = lambda:self.action(1)).grid(row = 1, column = 0)
        Button(master, text = "2", width = 11, command = lambda:self.action(2)).grid(row = 1, column = 1)
        Button(master, text = "3", width = 11, command = lambda:self.action(3)).grid(row = 1, column = 2)
        Button(master, text = "+", width = 11, command = lambda:self.action('+')).grid(row = 1, column = 3)
        Button(master, text = "4", width = 11, command = lambda:self.action(4)).grid(row = 2, column = 0)
        Button(master, text = "5", width = 11, command = lambda:self.action(5)).grid(row = 2, column = 1)
        Button(master, text = "6", width = 11, command = lambda:self.action(6)).grid(row = 2, column = 2)
        Button(master, text = "-", width = 11, command = lambda:self.action('-')).grid(row = 2, column = 3)
        Button(master, text = "7", width = 11, command = lambda:self.action(7)).grid(row = 3, column = 0)
        Button(master, text = "8", width = 11, command = lambda:self.action(8)).grid(row = 3, column = 1)
        Button(master, text = "9", width = 11, command = lambda:self.action(9)).grid(row = 3, column = 2)
        Button(master, text = "*", width = 11, command = lambda:self.action('*')).grid(row = 3, column = 3)
        Button(master, text = "0", width = 11, command = lambda:self.action(0)).grid(row = 4, column = 0)
        Button(master, text = "Clear", width = 11, command = lambda:self.clear()).grid(row = 4, column = 1)
        Button(master, text = "=", width = 57, command = lambda:self.calculate()).grid(row = 5, column = 0, columnspan = 4, padx = 10, pady = 10)
        Button(master, text = "/", width = 11, command = lambda:self.action("/")).grid(row = 4, column = 3)
        Button(master, text = ".", width = 11, command = lambda:self.action(".")).grid(row = 4, column = 2)


root = Tk()
GUI = Calculator(root)
root.mainloop()
