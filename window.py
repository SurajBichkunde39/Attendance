# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:10:21 2019

@author: lenovo
"""

import tkinter as tk
from processing import Processing
global selected_sub
global todays_attendance
todays_attendance = []
selected_sub = None

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
        self.process = Processing()
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
        self.fill_button_frame()

    def create_add_student_frame(self):
        self.add_student_frame = tk.Frame(root)
        self.add_student_frame.place(in_ = self.container , x=0 , y =0 ,relwidth = 1,relheight=1)
        
        tk.Label(self.add_student_frame,text = "Roll_number").grid(row = 0)
        tk.Label(self.add_student_frame,text = "First Name").grid(row = 1)
        tk.Label(self.add_student_frame,text = "Last Name").grid(row = 2)
        tk.Label(self.add_student_frame,text = "Mail id").grid(row = 3)
        tk.Label(self.add_student_frame,text = "date_of_Birth").grid(row = 4)

        self.e0 = tk.Entry(self.add_student_frame)
        self.e1 = tk.Entry(self.add_student_frame)
        self.e2 = tk.Entry(self.add_student_frame)
        self.e3 = tk.Entry(self.add_student_frame)
        self.e4 = tk.Entry(self.add_student_frame)

        self.e0.grid(row = 0,column = 1)
        self.e1.grid(row = 1,column = 1)
        self.e2.grid(row = 2,column = 1)
        self.e3.grid(row = 3,column = 1)
        self.e4.grid(row = 4,column = 1)

        done_button = tk.Button(self.add_student_frame , text = 'ADD' , command = self.add_stud_Action)
        quit_button = tk.Button(self.add_student_frame , text = 'Quit' , command = self.add_student_frame.destroy)
        done_button.grid(row = 5 , column = 0)
        quit_button.grid(row = 5, column = 1)

    def create_remove_student_frame(self):
        self.Remove_student_frame = tk.Frame(root)
        self.Remove_student_frame.place(in_ = self.container , x=0 , y =0 ,relwidth = 1,relheight=1)

        tk.Label(self.Remove_student_frame , text = 'Enetr Roll_number').grid(row = 1)
        self.e0 = tk.Entry(self.Remove_student_frame)
        self.e0.grid(row =  1 , column = 1)

        remove_button = tk.Button(self.Remove_student_frame , text  = 'Remove' , command = self.remove_stud_Action)
        quit_button = tk.Button(self.Remove_student_frame , text = 'Quit' , command = self.Remove_student_frame.destroy)
        remove_button.grid(row = 2 , column = 0)
        quit_button.grid(row = 2 , column = 1)

        
    def create_edit_student_frame(self):
        self.edit_student_frame = tk.Frame(root)
        self.edit_student_frame.place(in_ = self.container , x=0 , y =0 ,relwidth = 1,relheight=1)

        tk.Label(self.edit_student_frame,text = "Roll_number").grid(row = 0)
        tk.Label(self.edit_student_frame,text = "First Name").grid(row = 1)
        tk.Label(self.edit_student_frame,text = "Last Name").grid(row = 2)
        tk.Label(self.edit_student_frame,text = "Mail id").grid(row = 3)
        tk.Label(self.edit_student_frame,text = "date_of_Birth").grid(row = 4)

        self.e0 = tk.Entry(self.edit_student_frame)
        self.e1 = tk.Entry(self.edit_student_frame)
        self.e2 = tk.Entry(self.edit_student_frame)
        self.e3 = tk.Entry(self.edit_student_frame)
        self.e4 = tk.Entry(self.edit_student_frame)

        self.e0.grid(row = 0,column = 1)
        self.e1.grid(row = 1,column = 1)
        self.e2.grid(row = 2,column = 1)
        self.e3.grid(row = 3,column = 1)
        self.e4.grid(row = 4,column = 1)

        edit_button =  tk.Button(self.edit_student_frame , text  = 'Edit' , command = self.edit_stud_Action)
        quit_button = tk.Button(self.edit_student_frame , text = 'Quit' , command = self.edit_student_frame.destroy)
        edit_button.grid(row = 5 , column = 0)
        quit_button.grid(row = 5, column = 1)
        

    def edit_stud_Action(self):
        roll_no = self.e0.get()
        first = self.e1.get()
        last = self.e2.get()
        mail = self.e3.get()
        dob = self.e3.get()
        #will go for database action here
        print(roll_no,first,last,mail,dob)
        self.edit_student_frame.destroy()


    def remove_stud_Action(self):
        #will go for database action here
        roll_no = self.e0.get()
        print(roll_no)
        self.Remove_student_frame.destroy()

    def add_stud_Action(self):
        roll_no = self.e0.get()
        first = self.e1.get()
        last = self.e2.get()
        mail = self.e3.get()
        dob = self.e3.get()
        #will go for database action here
        print(roll_no,first,last,mail,dob)
        self.add_student_frame.destroy()

    def fill_button_frame(self):
        self.take_frame = tk.Frame(self.buttonFrame)
        self.report_frame = tk.Frame(self.buttonFrame)
        # self.info_frame = tk.Frame(self.buttonFrame)
        self.add_frame = tk.Frame(self.buttonFrame)
        self.sved_data = tk.Frame(self.buttonFrame)
        
        self.take_frame.pack()
        self.report_frame.pack()
        # self.info_frame.pack()
        self.add_frame.pack()
        self.sved_data.pack()
        
        bl = tk.Label(self.take_frame , text = 'Subbmit Attendence to Database' , bg= 'white', foreground = "red")
        bl.pack(side="top", fill="both", expand=True)
        b0 = tk.Button(self.take_frame, text="take_todays_attendence" , command = self.take_attendence_action)
        b0.pack(side = 'left')
        
        b1l = tk.Label(self.report_frame , text = 'Visualise Report' , bg= 'white', foreground = "red")
        b1l.pack(side="top", fill="both", expand=True)
        b1 = tk.Button(self.report_frame , text = "Sub_wise_report" , command = self.Sub_wise_report_Action)
        b1.pack(side = "left")
        
        
        
        b2l = tk.Label(self.add_frame , text = 'Get Info' , bg= 'white', foreground = "red")
        b2l.pack(side="top", fill="both", expand=True)
        b3 = tk.Button(self.add_frame , text = "get_student_info" , command = self.get_student_info_Action)
        b3.pack(side = "left")
        b3 = tk.Button(self.add_frame , text = "Check_Attendence_of_given_day" , command = self.Check_Attendence_of_given_day_Action)
        b3.pack(side = "left")
        
        b3l = tk.Label(self.sved_data , text = 'From Database' , bg= 'white', foreground = "red")
        b3l.pack(side="top", fill="both", expand=True)
        b4 = tk.Button(self.sved_data , text = "Add_Student" , command = self.add_Student_Action)
        b4.pack(side = "left")
        b5 = tk.Button(self.sved_data , text = "Remove_Student" , command = self.Remove_Student_Action)
        b5.pack(side = "left")
        b6 = tk.Button(self.sved_data , text = "Edit_student" , command = self.Edit_student_Action)
        b6.pack(side = "left")

    def Edit_student_Action(self):
        self.create_edit_student_frame()
        self.edit_student_frame.lift()

    def Remove_Student_Action(self):
        self.create_remove_student_frame()
        self.Remove_student_frame.lift()

    def add_Student_Action(self):
        self.create_add_student_frame()
        self.add_student_frame.lift()

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

    def select_sub_frame_Action1(self):
        global selected_sub
        selected_sub = 1
        self.attendence_frame.lift()

    def select_sub_frame_Action2(self):
        global selected_sub
        selected_sub = 2
        self.attendence_frame.lift()

    def select_sub_frame_Action3(self):
        global selected_sub
        selected_sub = 3
        self.attendence_frame.lift()

    def select_sub_frame_Action4(self):
        global selected_sub
        selected_sub = 1
        self.attendence_frame.lift()

    def select_sub_frame_Action5(self):
        global selected_sub
        selected_sub = 1
        self.attendence_frame.lift()
    
    def add_sub_from_str(self,sub_str):
        sub_lst  = sub_str.split(',')
        b1 = tk.Button(self.select_sub_frame, text=sub_lst[0], command=self.select_sub_frame_Action1)
        b1.pack(side="top", fill="both", expand=True)
        b1 = tk.Button(self.select_sub_frame, text=sub_lst[1], command=self.select_sub_frame_Action2)
        b1.pack(side="top", fill="both", expand=True)
        b1 = tk.Button(self.select_sub_frame, text=sub_lst[2], command=self.select_sub_frame_Action3)
        b1.pack(side="top", fill="both", expand=True)
        b1 = tk.Button(self.select_sub_frame, text=sub_lst[3], command=self.select_sub_frame_Action4)
        b1.pack(side="top", fill="both", expand=True)
        b1 = tk.Button(self.select_sub_frame, text=sub_lst[4], command=self.select_sub_frame_Action5)
        b1.pack(side="top", fill="both", expand=True)

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
        global selected_sub
        todays_attendance.sort()
        todays_attendance_copy = [str(x) for x in todays_attendance]
        csv_attn = ','.join(todays_attendance_copy)
        self.process.take_attendence(csv_attn,selected_sub)
        self.root.destroy()

    def get_student_info_Action(self):
        self.info_frame = tk.Frame(root)
        self.info_frame.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self.info_frame , text = 'Enetrt Roll Number').grid(row = 0)
        self.e1 = tk.Entry(self.info_frame)
        self.e1.grid(row = 0,column = 1)

        search_button = tk.Button(self.info_frame , text = "Search" , command = self.search_Action)
        search_button.grid(row = 1,column = 0)
        quit_button = tk.Button(self.info_frame , text = 'Quit' , command = self.info_frame.destroy)
        quit_button.grid(row = 1 , column = 1)


    def search_Action(self):
        roll = self.e1.get()
        tup = self.process.give_info_of_student(roll)
        first_name = tup[1]
        last_name = tup[2]
        mail = tup[3]
        dob = tup[4]

        info = tk.Frame(root)
        info.place(in_ = self.container , x=0, y=0, relwidth=1, relheight=1)
        
        tk.Label(info , text = 'Roll Number').grid(row = 0 , column = 0)
        tk.Label(info , text = roll).grid(row = 0 , column  = 1)
        tk.Label(info , text = 'First Name').grid(row = 1 , column = 0)
        tk.Label(info , text = first_name).grid(row = 1 , column  = 1)
        tk.Label(info , text = 'Last Name').grid(row = 2 , column = 0)
        tk.Label(info , text = last_name).grid(row = 2 , column  = 1)
        tk.Label(info , text = 'Mail Id').grid(row = 3 , column = 0)
        tk.Label(info , text = mail).grid(row = 3 , column  = 1)
        tk.Label(info , text = 'Date of Birth').grid(row = 4 , column = 0)
        tk.Label(info , text = dob).grid(row = 4 , column  = 1)
        
        quit_button = tk.Button(info , text = 'Quit' , command = info.destroy)
        quit_button.grid(row = 5 , column = 0)
        
    def Check_Attendence_of_given_day_Action(self):
        self.get_date_frame = tk.Frame(root)
        self.get_date_frame.place(in_ = self.container , x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self.get_date_frame , text = 'Eneter the date for you want Attendence(yyyy-mm-dd)').grid(row = 0)
        self.e1 = tk.Entry(self.get_date_frame)
        self.e1.grid(row = 1,column = 0)

        search_Date = tk.Button(self.get_date_frame , text = "Search" , command = self.search_Date_Action)
        search_Date.grid(row = 2,column = 0)
        quit_button = tk.Button(self.get_date_frame , text = 'Quit' , command = self.get_date_frame.destroy)
        quit_button.grid(row = 3 , column = 0)

    def search_Date_Action(self):
        #will go for database action here
        date1 = self.e1.get()
        presenty = self.process.get_attendence_of_day(date1)
        
        presenty_of_given_date = tk.Frame(root)
        presenty_of_given_date.place(in_ = self.container , x=0, y=0, relwidth=1, relheight=1)
        i = 0
        for item in presenty:
            tk.Label(presenty_of_given_date , text = str(item[1])+'-->'+item[0]).grid(row = i)
            i+=1
        quit_button = tk.Button(presenty_of_given_date , text = 'Quit' , command = presenty_of_given_date.destroy)
        quit_button.grid(row = i , column = 0)

    def Sub_wise_report_Action(self):
        dates_frame = tk.Frame(root)
        dates_frame.place(in_ = self.container , x=0, y=0, relwidth=1, relheight=1)
        tk.Label(dates_frame,text = 'Enetr starting and final dates (yyyy/mm/dd) for making report').grid(row = 0)
        tk.Label(dates_frame,text = 'Starting Date : ').grid(row = 1 , column = 0)
        tk.Label(dates_frame,text = 'Ending Date : ').grid(row = 2 , column = 0)
        tk.Label(dates_frame,text = 'Sub Id : ').grid(row = 3 , column = 0)
        self.e1 = tk.Entry(dates_frame)
        self.e2 = tk.Entry(dates_frame)
        self.e3 = tk.Entry(dates_frame)
        self.e1.grid(row = 1 , column = 1)
        self.e2.grid(row = 2 , column = 1)
        self.e3.grid(row = 3 , column = 1)
        gen_graph = tk.Button(dates_frame,text = 'generate_graph' , command = self.gen_graphAction)
        gen_graph.grid(row = 4 , column = 0)
        quit_button = tk.Button(dates_frame , text = 'Quit' , command = dates_frame.destroy)
        quit_button.grid(row = 5 , column = 0)

    def gen_graphAction(self):
        day1 = self.e1.get()
        day2 = self.e2.get()
        sub = self.e3.get()
        self.process.sub_wise_weekly_report(day1,day2,sub)


root = tk.Tk()
window = MainView(root)
root.geometry('450x480')
window.add_menubar()
sub_str = 'SEPM,ISEE,TOC,CN,DBMS'
window.add_sub_from_str(sub_str)
window.add_attendence_sheet(16)
root.mainloop()