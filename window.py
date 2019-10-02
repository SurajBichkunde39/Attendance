# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:10:21 2019

@author: lenovo
"""

import tkinter as tk
root = tk.Tk()
global todays_attendance
todays_attendance = []

class Roll_number:
    def __init__(self,frame,roll):
        self.master = frame
        self.roll = roll
        self.row = int((self.roll) /10)
        self.col = (self.roll) % 10 
        self.clicked = False
    def add_but(self):
        
        if not self.clicked:
            self.Button1 = tk.Button(self.master, text="   {}   ".format(str(self.roll)), command = self.change_color,bg="Black", fg="White")
            
        else:
            self.Button1 = tk.Button(self.master, text="   {}   ".format(str(self.roll)), command = self.change_color,bg="red", fg="White")
        self.Button1.grid(row=self.row, column=self.col)
        self.Button1.config(height =3, width = 5)
        
        
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


class MainView(object):
    def __init__(self,root):
        self.root = root
        self.buttonFrame = tk.Frame(root)
        self.container    = tk.Frame(root)
        self.buttonFrame.pack(side = 'top',fill = 'x',expand = False)
        self.container.pack(side = 'top',fill = 'both',expand = True)

        self.login_frame = tk.Frame(root) 
        self.select_sub_frame = tk.Frame(root)
        self.attendence_frame = tk.Frame(root)
        self.graph_frame = tk.Frame(root)

        self.login_frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.select_sub_frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.attendence_frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.graph_frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        self.roll_numbers_frame = tk.Frame(self.attendence_frame)
        self.subbmit_button_frame = tk.Frame(self.attendence_frame)
        self.roll_numbers_frame.pack(side="top", fill="both", expand=True)
        self.subbmit_button_frame.pack(side="top")
        # self.subbmit_button_frame.place(in_=self.attendence_frame, x=0, y=0, relwidth=1, relheight=1)
        #self.subbmit_button_frame.pack()
        self.fill_button_frame()

    def fill_button_frame(self):
        self.take_frame = tk.Frame(self.buttonFrame)
        self.report_frame = tk.Frame(self.buttonFrame)
        self.info_frame = tk.Frame(self.buttonFrame)
        self.add_frame = tk.Frame(self.buttonFrame)
        self.sved_data = tk.Frame(self.buttonFrame)
        
        self.take_frame.pack()
        self.report_frame.pack()
        self.info_frame.pack()
        self.add_frame.pack()
        self.sved_data.pack()
        
        bl = tk.Label(self.take_frame , text = 'Subbmit Attendence to Database' , bg= 'white', foreground = "red")
        bl.pack(side="top", fill="both", expand=True)
        b0 = tk.Button(self.take_frame, text="take_attendence" , command = self.take_attendence_action)
        b0.pack(side = 'left')
        b10 = tk.Button(self.take_frame, text="Add_attendence_to_given_date")
        b10.pack(side = 'left')
        
        b1l = tk.Label(self.report_frame , text = 'Visualise Report' , bg= 'white', foreground = "red")
        b1l.pack(side="top", fill="both", expand=True)
        #b1 = tk.Button(self.report_frame , text = "Monthly Report")
        #b1.pack(side = "left")
        b1 = tk.Button(self.report_frame , text = "Sub_wise_weekly_report")
        b1.pack(side = "left")
        b2 = tk.Button(self.report_frame , text = "Sub_wise_monthly_report")
        b2.pack(side = "left")
        
        
        b2l = tk.Label(self.add_frame , text = 'Get Info' , bg= 'white', foreground = "red")
        b2l.pack(side="top", fill="both", expand=True)
        b3 = tk.Button(self.add_frame , text = "get_student_info")
        b3.pack(side = "left")
        b3 = tk.Button(self.add_frame , text = "Check_Attendence_of_given_day")
        b3.pack(side = "left")
        
        b3l = tk.Label(self.sved_data , text = 'From Database' , bg= 'white', foreground = "red")
        b3l.pack(side="top", fill="both", expand=True)
        b4 = tk.Button(self.sved_data , text = "Add_Student")
        b4.pack(side = "left")
        b5 = tk.Button(self.sved_data , text = "Remove_Student")
        b5.pack(side = "left")
        b6 = tk.Button(self.sved_data , text = "Edit_student")
        b6.pack(side = "left")


    def add_menubar(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu = self.menubar)
        subMenu = tk.Menu(self.menubar , tearoff = 0)
        self.menubar.add_cascade(label = 'Instructor',menu = subMenu)
        subMenu.add_command(label = 'Add Student')
        subMenu.add_command(label = 'Edit Student')

        subMenu2 = tk.Menu(self.menubar , tearoff = 0)
        self.menubar.add_cascade(label = 'Student',menu = subMenu2)
        subMenu2.add_command(label = 'Track Me')
        subMenu2.add_command(label = 'Ask Questions')

        subMenu3 = tk.Menu(self.menubar , tearoff = 0)
        self.menubar.add_cascade(label = 'Summary',menu = subMenu3)
        subMenu3.add_command(label = 'Weekly Report')
        subMenu3.add_command(label = 'Monthly Report')
    
    def take_attendence_action(self):
        self.buttonFrame.pack_forget()
        self.select_sub_frame.lift()

    def add_subject_button(self , sub_name):
        b1 = tk.Button(self.select_sub_frame, text=sub_name, command=self.attendence_frame.lift)
        b1.pack(side="top", fill="both", expand=True)

    def add_sub_from_str(self,sub_str):
        sub_lst  = sub_str.split(',')
        for item in sub_lst:
            self.add_subject_button(item)

    def add_subbmit_but(self):
        sub_but = tk.Button(self.subbmit_button_frame,text = "Subbmit",command = self.get_todays_attendence)
        sub_but.pack(side="top", fill="both", expand=True)

    def add_attendence_sheet(self , number_of_student):
        for i in range(1,number_of_student+1):
            cap = Roll_number(self.roll_numbers_frame,i)
            cap.add_but()
        self.add_subbmit_but()

    def get_todays_attendence(self):
        global todays_attendance
        todays_attendance.sort()
        todays_attendance_copy = [str(x) for x in todays_attendance]
        csv_attn = ','.join(todays_attendance_copy)
        print(csv_attn)
        self.root.destroy()

window = MainView(root)
root.geometry('450x480')
window.add_menubar()
sub_str = 'SEPM,ISEE,TOC,CN,DBMS'
window.add_sub_from_str(sub_str)
window.add_attendence_sheet(16)
root.mainloop()