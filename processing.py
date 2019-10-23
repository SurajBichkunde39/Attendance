# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:59:19 2019

@author: lenovo
"""
import mysql.connector
from matplotlib import pyplot as plt
import datetime

class Processing(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root123',
            database = 'prodb_sample')
        self.mycursor = self.mydb.cursor(buffered=True)
    
    def take_attendence(self,str1 , sub_id):
        today = datetime.datetime.now()
        p_date = '-'.join([str(x) for x in [today.year,today.month,today.day]])
        total_presenty = len(str1)
        values = (p_date,str1,total_presenty,sub_id)
        query = 'INSERT INTO attendence VALUES (%s,%s,%s,%s)'
        self.mycursor.execute(query,values)
        self.mydb.commit()
        
    def add_presenty_of_day(self , day):
        pass

    def sub_wise_weekly_report(self , date1, date2 , sub_id1):
        # print(date1, date2 , sub_id1)
        query = 'SELECT p_date , total_presenty , sub_id FROM  attendence WHERE sub_id = %s AND p_date >= %s AND p_date <= %s '
        values = (sub_id1,date1,date2)
        self.mycursor.execute(query,values)
        x = []
        y = []
        for item in self.mycursor:
            #print(item[1])
            x.append(item[0])
            y.append(item[1])
        # print(y)
        # print(x)
        temp_x = [x for x in range(1,len(y)+1)]
        plt.bar(temp_x,y)
        plt.xlabel('ith day in given interval')
        plt.ylabel('total presenty')
        plt.title('Attendance Report')
        plt.show()
        
    def give_info_of_student(self,roll_no):
        query = 'SELECT * FROM student WHERE roll_no = %s'
        value = (roll_no,)
        self.mycursor.execute(query,value)
        for item in self.mycursor:
            return item
        
    def add_student(self,roll_no,first_name,last_name,dob,mail):
        self.mycursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s)",(roll_no,first_name,last_name,dob,mail))
        self.mydb.commit()
        
    def remove_student(self,roll_no):
        query = 'DELETE FROM student WHERE roll_no = %s'
        value = (roll_no,)
        self.mycursor.execute(query,value)
        self.mydb.commit()
    def update_student_info(self,roll_no,first_name,last_name,mail,dob):
        new_info = [roll_no,first_name,last_name,dob,mail]
        orignal_info = self.give_info_of_student(roll_no)
        changing_tup = []
        for a,b in zip(orignal_info,new_info):
            if b == '' or a==b:
                changing_tup.append(a)
            else:
                changing_tup.append(b)
        query = 'UPDATE student set First_name = %s , Last_name = %s, date_of_birth = %s ,mail = %s WHERE roll_no = %s'
        value = (changing_tup[1] , changing_tup[2] , changing_tup[3] ,changing_tup[4] , changing_tup[0])
        self.mycursor.execute(query,value)
        self.mydb.commit()
        
    def get_attendence_of_day(self,date1):
        query = 'select s.presenty_str , su.sub_name from attendence as s , subject as su where p_date=%s and s.sub_id = su.sub_id'
        value = (date1,)
        attens = []
        self.mycursor.execute(query,value)
        for item in self.mycursor:
            attens.append((item[0],item[1]))
        return attens
    
    
    def give_total_number_of_student(self):
        self.mycursor.execute('SELECT COUNT(*) FROM student')
        for item in self.mycursor:
            return item[0]
        
if __name__ == '__main__':
    
    pr = Processing()
    for item in pr.get_attendence_of_day('2019/09/11'):
        print(item)
    