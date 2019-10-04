import random
import datetime
import mysql.connector
mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root123',
            database='prodb_sample')
mycursor = mydb.cursor(buffered=True)
d_starting = datetime.datetime(2019,7,1)

for i in range(0,95):
	is_weekday = d_starting.weekday()
	sub_id_lst = [1,2,3,4,5]
	if is_weekday != 5 and is_weekday != 6:
		number_of_present_student = []
		for j in range(0,4):
			number_of_present_student.append(random.randint(8,16))
		lec_1 = random.sample(range(1, 17), number_of_present_student[0])
		lec_2 = random.sample(range(1, 17), number_of_present_student[1])
		lec_3 = random.sample(range(1, 17), number_of_present_student[2])
		lec_4 = random.sample(range(1, 17), number_of_present_student[3])
		lec = [lec_1 , lec_2 , lec_3 , lec_4]
		sub_id_lst.remove(is_weekday + 1)
		y = str(d_starting.year)
		m = str(d_starting.month)
		d = str(d_starting.day)
		p_date1 = [y,m,d]
		p_date1 = '-'.join(p_date1)
		for m in range(0,4):
			sub_id1 = sub_id_lst[m]
			total_pre = len(lec[m])
			pre_str = ','.join([str(x)for x in lec[m]])
			mycursor.execute("INSERT INTO attendence VALUES (%s,%s,%s,%s)",(p_date1,pre_str,total_pre,sub_id1))
			mydb.commit()
	d_starting += datetime.timedelta(days=1)
