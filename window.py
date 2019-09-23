# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:10:21 2019

@author: lenovo
"""

import tkinter as tk
from student import Student
window = tk.Tk()


class LoginPage:
    def __init__(self,master):
        self.master = master
    
    def login_lable(self):
        print('i am here')
        self.username = tk.Label(self.master , text = "Username: ")
        self.username.grid(row = 0 , column = 0)
        self.usern = tk.Entry(self.master)
        self.usern.grid(row=0, column=1, sticky=tk.E)
        self.passward = tk.Label(self.master , text = "Password: ")
        self.passward.grid(row = 1 , column = 0)
        self.passn = tk.Entry(self.master)
        self.passn.grid(row=2, column=1, sticky=tk.E)
        self.login = tk.Button(self.master,text="log in")
        self.login.grid(row = 3 , column = 0)


class Roll_number:

    def __init__(self,frame,roll):
        self.master = frame
        self.roll = roll
        self.row = int((roll) /10)
        self.col = (roll) % 10 
        self.clicked = False
    def add_but(self):
        
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

class MainWndow:
    def __init__(self,window):
        self.window = window
        self.Attendence = tk.Frame(window)
        self.Attendence.pack()
        self.menubar = tk.Menu(window)
        window.config(menu = self.menubar)
        
        subMenu = tk.Menu(self.menubar , tearoff = 0)
        self.menubar.add_cascade(label = 'Instructor',menu = subMenu)
        subMenu.add_command(label = 'Add Student')
        subMenu.add_command(label = 'Edit Student')
        
        
        subMenu2 = tk.Menu(self.menubar , tearoff = 0)
        self.menubar.add_cascade(label = 'Student',menu = subMenu)
        subMenu2.add_command(label = 'Track Me')
        subMenu2.add_command(label = 'Ask Questions')

    def add_student(self):
        for i in range(1,67):
            cap = Roll_number(self.Attendence , i)
            cap.add_but()
            
    def submit_attendence(self):
        pass

    

mainwin = MainWndow(window)
mainwin.add_student()
window.mainloop()