# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:31:49 2019

@author: lenovo
"""
import datetime

class Student:
    def __init__(self,roll_no,first_name,last_name,**kwarg):
        self.first_name = first_name
        self.last_name = last_name
        self.roll_no = int(roll_no)
        self.email = None
        self.date_of_birth = None
        self.age = None
        for key , value in kwarg.items():
            if key == 'email':
                self.set_mail(value)
            elif key == 'date_of_birth':
                self.set_date_of_birth(value)
    
    def set_mail(self,mail):
        self.email = mail
        
    def set_date_of_birth(self,str1):
        year = month = day = None
        print(str1)
        if '/' in str1:
            year , month , day = str1.split('/')
        elif '\\' in str1:
            year , month , day = str1.split('\\')
        elif '-' in str1:
            year , month , day = str1.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        self.date_of_birth = datetime.datetime(int(year),int(month),int(day))
        self.age = self.get_age()

    def get_age(self):
            
        today = datetime.date.today()
        dob = self.date_of_birth
        years = today.year - dob.year
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            years -= 1
        return years
        
    def print_everthing(self):
        print('first Name = ' , self.first_name)
        print('Last Name = ' , self.last_name)
        print('date of birth = ', self.date_of_birth)
        print('age = ' ,self.age)
    
#testing
if __name__ == '__main__':
    std1 = Student(1,'suraj','bichkunde')
    std2 = Student(2,'Kapil', 'Sharma',email = 'ssbwork39', date_of_birth = '1999/09/19')
    std2.print_everthing()
    std1.set_date_of_birth('2000/1/1')
    std1.print_everthing()
    

        
        