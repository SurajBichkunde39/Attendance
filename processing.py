# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:59:19 2019

@author: lenovo
"""
import mysql.connector
import pandas as pd
from matplotlin import pyplot as plt

class Processing(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root123')
        self.mycursor = self.mydb.cursor(buffered=True)
    
    def take_attendence(self , date):
    	pass

    def add_presenty_of_day(self , day):
    	pass

    def sub_wise_weekly_report(self , sub_id):
        pass
    
    def sub_wise_monthly_report(self , sub_id):
    	pass

    def get_students_info(self,roll_no):
    	pass

    def get_attendence_of_given_day(self , date):
    	pass

    def add_student(self , stud):
    	pass

    def remove_student(self,stud):
    	pass

    def edit_student(self,stud):
    	pass

    def plot_mothely_report(self dates , at_lst):
    	pass

    def plot_weekly_report(self , weeks , at_lst):
    	pass