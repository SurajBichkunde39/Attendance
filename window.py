# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:10:21 2019

@author: lenovo
"""

import tkinter as tk
from student import Student
window = tk.Tk()

global todays_attendance
todays_attendance = []

class LoginPage:
    '''
    i am not sure about the exact use of this class 
    master is the frame , i am going to lift this on the top of mainwin
    '''
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
    '''
    this is roll_number button every student is associated with this class
    '''
    def __init__(self,frame,stud):
        self.master = frame
        self.stud = stud
        self.roll = stud.roll_no
        self.row = int((self.roll) /10)
        self.col = (self.roll) % 10 
        self.clicked = False
    def add_but(self):
        
        if not self.clicked:
            self.Button1 = tk.Button(self.master, text="   {}   ".format(str(self.roll)), command = self.change_color,bg="Black", fg="White")
            
        else:
            self.Button1 = tk.Button(self.master, text="   {}   ".format(str(self.roll)), command = self.change_color,bg="red", fg="White")
        self.Button1.grid(row=self.row, column=self.col)
        self.Button1.config(height =2, width = 3)
        
        
    def change_color(self):
        global todays_attendance
        if not self.clicked:
            self.clicked = True
            self.add_but()
            todays_attendance.append(self.roll)
        else:
            self.clicked = False
            self.add_but()
            todays_attendance.remove(self.roll)

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
        self.submit_button()

    def add_student(self , stud):
        cap = Roll_number(self.Attendence , stud)
        cap.add_but()
    
            
    def submit_button(self):
        self.submit = tk.Button(self.window, text="   submit   ",command = self.submit_attendence,bg="green", fg="white")
        self.submit.pack()
    
    def submit_attendence(self):
        global todays_attendance
        todays_attendance.sort()
        print(todays_attendance)


class Solution(object):
    '''
    solution class will note down todays attendence and add it to one csv file
    csv structure will be -> date , present_roll_numbers(csv)
    '''
    def __init__(self , mainwin):
        self.mainwin = mainwin
    
    def add_student_with_csv(self,csv_filename):
        all_data = []
        with open(csv_filename) as f:
            all_data = f.readlines()
    
        for i in range(1,len(all_data)):
            roll,f_name,l_name,dob,mail = all_data[i].split(',')
            std = Student(roll,f_name,l_name,date_of_birth = dob , email = mail)
            self.mainwin.add_student(std)
    
   
    
    
mainwin = MainWndow(window)
sol = Solution(mainwin)
sol.add_student_with_csv('students_info.txt')
window.mainloop()