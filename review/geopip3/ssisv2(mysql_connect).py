import mysql.connector
from mysql.connector import Error

id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
gender = input("Enter Gender (M/F): ")
year_level = input("Enter Student Year Level: ")
course = input("Enter Course: ")
course_code = input("Enter Course Code (ex. BSCS): ")

try:
    con = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='ssis123',
    database='ssis_v2'
    )
    query = "INSERT INTO students (ID, NAME, GENDER, YEAR_LEVEL, COURSE, COURSE_CODE) VALUES ('" + id + "', '" + name + "', '" + gender + "', '" + course + "', '" + course_code + "' )"
    cur = con.cursor()
    cur.execute(query) 
    con.commit()
    cur.close()

    print("Successfully Inserted Record!")
except Error as error:
    print("Insert data failed {}".format(error))
finally:
    if con.is_connected():
        con.close()
        print("mysql connection closed")
        

"""
cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='ssis123',
    database='ssis_v2'
)
"""

