# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:10:21 2019

@author: lenovo
"""

import tkinter as tk


window = tk.Tk()

#menuframe = tk.Frame(window)
#menuframe.pack()
menubar = tk.Menu(window)
window.config(menu = menubar)


subMenu = tk.Menu(menubar , tearoff = 0)
menubar.add_cascade(label = 'Instructor',menu = subMenu)
subMenu.add_command(label = 'Add Student')
subMenu.add_command(label = 'Edit Student')


subMenu = tk.Menu(menubar , tearoff = 0)
menubar.add_cascade(label = 'Student')
subMenu.add_command(label = 'Track Me')
subMenu.add_command(label = 'Ask Questions')


Attendence = tk.Frame(window)
Attendence.pack()

class Roll_number:

    def __init__(self,frame,roll):
        self.master = frame
        self.roll = roll
        self.row = int((roll) /10)
        self.col = (roll) % 10 
        self.clicked = False
    def add_but(self):
        print(self.roll , self.row,self.col)
        if not self.clicked:
            self.Button1 = tk.Button(self.master, text="   {}   ".format(str(self.roll)), command = self.change_color,bg="Black", fg="White")
            
        else:
            self.Button1 = tk.Button(self.master, text="   {}   ".format(str(self.roll)), command = self.change_color,bg="red", fg="White")
        self.Button1.grid(row=self.row, column=self.col)
        self.Button1.config(height =2, width = 3)
        
        
    def change_color(self):
        if not self.clicked:
            self.clicked = True
            self.add_but()
        else:
            self.clicked = False
            self.add_but()
        
        

for i in range(1,67):
    cap = Roll_number(Attendence , i)
    cap.add_but()
window.mainloop()