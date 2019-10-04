import mysql.connector
import pandas as pd

class Database(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root123')
        self.mycursor = self.mydb.cursor(buffered=True)
        self.get_database()

    def get_database(self):
        yes = False
        self.mycursor.execute('SHOW DATABASES')
        for databasename in self.mycursor:
            if databasename[0] == 'prodb_sample':
                self.mydb.database = 'prodb_sample'
                yes = True
                break
        if not yes:
            self.create_database()

    def create_database(self):
        self.mycursor.execute('CREATE DATABASE prodb_sample')
        self.create_tables()

    def create_tables(self):
        self.mycursor.execute('CREATE TABLE student (Roll_no INT PRIMARY KEY, First_name VARCHAR(20) , Last_name VARCHAR(20),date_of_birth DATE ,mail VARCHAR(30))')
        self.mycursor.execute('CREATE TABLE subject (sub_id INT PRIMARY KEY , sub_name VARCHAR(20))')
        self.mycursor.execute('CREATE TABLE instructor (Ins_id INT PRIMARY KEY , First_name VARCHAR(20),Last_name VARCHAR (20),edu VARCHAR(20),sub_id int ,FOREIGN KEY(sub_id) REFERENCES subject(sub_id))')
        self.mycursor.execute('CREATE TABLE attendence(p_date DATE PRIMARY KEY , presenty_str VARCHAR(200) , total_presenty INT , sub_id INT , FOREIGN KEY (sub_id) REFERENCES subject(sub_id))')
        self.mydb.commit()

    def table_not_present(self):
        self.mycursor.execute('SHOW TABLES')
        for item in self.mycursor:
            if 'student' == item[0]:
                return False
        return True

    def add_students_with_csv(self,filename):
        df = pd.read_csv(filename)
        if self.table_not_present():
            self.create_tables()
        for index,row in df.iterrows():
            self.add_student(row['roll_no'],row['first_name'],row['last_name'],row['date_of_birth'],row['email'])
            
    def add_student(self,roll_no,first_name,last_name,dob,mail):
        #print(roll_no,first_name,last_name,dob,mail)
        self.mycursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s)",(roll_no,first_name,last_name,dob,mail))
        self.mydb.commit()
    

    def show_all_student(self):
        self.mycursor.execute('SELECT * FROM student')
        for item in self.mycursor:
            print(item)

#testing
if __name__ == '__main__':
    db = Database()
    db.add_students_with_csv('students_info.txt')
    db.show_all_student()
