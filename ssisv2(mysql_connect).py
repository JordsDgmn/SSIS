import mysql.connector
from mysql.connector import Error

def search_student():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )

        print("[ press enter key to cancel ]")
        search_choice = input("\n\nSearch by: \n\n1. Student ID\n2. Student Name\n\nEnter your choice: ")
        if search_choice == '':
            print("Search canceled.")
            return
        elif search_choice not in ['1', '2']:
            print("Invalid choice. Please enter a valid option.")
            return

        if search_choice == '1':
            student_id = input("Enter student ID to search: ")
            query = "SELECT * FROM students WHERE ID = %s"
            values = (student_id,)
        elif search_choice == '2':
            student_name = input("Enter student name to search: ")
            query = "SELECT * FROM students WHERE NAME = %s"
            values = (student_name,)

        cursor = con.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            print("\n \n -----Student found!-----")
            print("Student ID:", result[0])
            print("Student Name:", result[1])
            print("Gender:", result[2])
            print("Year Level:", result[3])
            print("Course:", result[4])
            print("Course Code:", result[5])
        else:
            print("!- - - -Student not found.- - - -!")

        cursor.close()
    except Error as error:
        print("Error occurred while searching for student:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")

def insert_student():


    try:
        con = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='ssis123',
        database='ssis_v2'
        )
        student_id = input("[ press enter key to cancel ] \n \n Enter student ID: ")
        if student_id == "":
            return
        name = input("Enter Student Name: ")
        gender = input("Enter Gender (M/F): ")
        year_level = input("Enter Student Year Level: ")
        course = input("Enter Course: ")
        course_code = input("Enter Course Code (ex. BSCS): ")
        
        query = "INSERT INTO students (ID, NAME, GENDER, YEAR_LEVEL, COURSE, COURSE_CODE) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (student_id, name, gender, year_level, course, course_code)

        cursor = con.cursor()
        cursor.execute(query, values)
        con.commit()
        cursor.close()

        print("Successfully Inserted Record!")
    except Error as error:
        print("Insert data failed:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")
            
def update_student_info():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )

        query = "SELECT ID, NAME FROM students"
        cursor = con.cursor()
        cursor.execute(query)
        students = cursor.fetchall()

        if students:
            print("List of Students:")
            for i, student in enumerate(students, start=1):
                print(f"{i}.) {student[0]}, {student[1]}")

            while True:
                student_choice = input("[ press enter key to cancel ] \n \n Enter student number to edit: ")
                if student_choice == '':
                    print("Update canceled.")
                    return
                elif not student_choice.isdigit() or int(student_choice) < 1 or int(student_choice) > len(students):
                    print("Invalid input. Please enter a valid number.")
                else:
                    break

            student_id = students[int(student_choice) - 1][0]
            query = "SELECT * FROM students WHERE ID = %s"
            values = (student_id,)

            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                print("\n \n -----Current Student Information-----")
                print("Student ID:", result[0])
                print("Student Name:", result[1])
                print("Gender:", result[2])
                print("Year Level:", result[3])
                print("Course:", result[4])
                print("Course Code:", result[5])
                
                new_student_id = input("Enter new student ID (leave empty to keep the same): ")
                new_name = input("Enter new name (leave empty to keep the same): ")
                new_gender = input("Enter new gender (M/F) (leave empty to keep the same): ")
                new_year_level = input("Enter new year level (leave empty to keep the same): ")
                new_course = input("Enter new course (leave empty to keep the same): ")
                new_course_code = input("Enter new course code (leave empty to keep the same): ")
                

                if new_name or new_gender or new_year_level or new_course or new_course_code or new_student_id:
                    update_query = "UPDATE students SET NAME = %s, GENDER = %s, YEAR_LEVEL = %s, COURSE = %s, COURSE_CODE = %s, ID = %s WHERE ID = %s"
                    update_values = (
                        new_student_id if new_student_id else result[0],
                        new_name if new_name else result[1],
                        new_gender if new_gender else result[2],
                        new_year_level if new_year_level else result[3],
                        new_course if new_course else result[4],
                        new_course_code if new_course_code else result[5],
                        
                        student_id
                    )

                    cursor.execute(update_query, update_values)
                    con.commit()
                    print("Student information updated successfully!")
                else:
                    print("No changes made to student information.")
            else:
                print("!- - - -Student not found.- - - -!")

        else:
            print("No students found.")

        cursor.close()
    except Error as error:
        print("Error occurred while updating student information:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")

def delete_student():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )

        
        query = "SELECT ID, NAME FROM students"
        cursor = con.cursor()
        cursor.execute(query)
        students = cursor.fetchall()

        if students:
            print("List of Students:")
            for i, student in enumerate(students, start=1):
                print(f"{i}.) {student[0]}, {student[1]}")

            
            while True:
                student_choice = input("[ press enter key to cancel ] \n \n Enter the number of the student to delete: ")
                if student_choice == '':
                    print("Deletion canceled.")
                    return
                elif not student_choice.isdigit() or int(student_choice) < 1 or int(student_choice) > len(students):
                    print("Invalid input. Please enter a valid number.")
                else:
                    break

           
            student_id = students[int(student_choice) - 1][0]
            query = "DELETE FROM students WHERE ID = %s"
            values = (student_id,)
            cursor.execute(query, values)
            con.commit()

            if cursor.rowcount > 0:
                print("\n Student deleted successfully!")
            else:
                print("!- - - -Student not found.- - - -!")

        else:
            print("No students found.")

        cursor.close()
    except Error as error:
        print("Error occurred while deleting student:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")

def list_students():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )
        query = "SELECT ID, NAME, COURSE FROM students"

        cursor = con.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("\n \n -----List of Students-----")
            for row in result:
                print("Student ID:", row[0])
                print("Student Name:", row[1])
                print("Course:", row[2])
                print("------------------------")
        else:
            print("No students found.")

        cursor.close()
    except Error as error:
        print("Error occurred while listing students:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")

def search_course():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )

        print("[ press enter key to cancel ]")
        search_choice = input("\n\nSearch by: \n\n1. Course ID\n2. Course Name\n\nEnter your choice: ")
        if search_choice == '':
            print("Search canceled.")
            return
        elif search_choice not in ['1', '2']:
            print("Invalid choice. Please enter a valid option.")
            return

        if search_choice == '1':
            course_id = input("Enter course ID to search: ")
            query = "SELECT * FROM courses WHERE course_id = %s"
            values = (course_id,)
        elif search_choice == '2':
            course_name = input("Enter course name to search: ")
            query = "SELECT * FROM courses WHERE course_name = %s"
            values = (course_name,)

        cursor = con.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            print("\n -----Course found!-----\n ")
            print("Course ID:", result[0])
            print("Course Name:", result[1])
        else:
            print("!- - - -Course not found.- - - -!")

        cursor.close()
    except Error as error:
        print("Error occurred while searching for course:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")

            
            
            
            
def insert_course():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )
        course_id = input("[ press enter key to cancel ] \n \n Enter course ID: ")
        if course_id == "":
            return
        course_name = input("[ press enter key to cancel ] \n \n Enter course name: ")
        
        query = "INSERT INTO courses (course_id, course_name) VALUES (%s, %s)"
        values = (course_id, course_name)

        cursor = con.cursor()
        cursor.execute(query, values)
        con.commit()

        print("Successfully inserted course!")
    except Error as error:
        print("Insert data failed:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")
            
def list_courses():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )
        query = "SELECT course_id, course_name FROM courses"

        cursor = con.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("\n \n -----List of Courses-----")
            for row in result:
                print("Course ID:", row[0])
                print("Course Name:", row[1])
                print("------------------------")
        else:
            print("No courses in database. Feel free to add.")

        cursor.close()
    except Error as error:
        print("Error occurred while listing courses:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")            
 
def update_course_info():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )

        query = "SELECT course_id, course_name FROM courses"
        cursor = con.cursor()
        cursor.execute(query)
        courses = cursor.fetchall()

        if courses:
            print("List of Courses:")
            for i, course in enumerate(courses, start=1):
                print(f"{i}.) {course[0]}, {course[1]}")

            while True:
                course_choice = input("[ press enter key to cancel ] \n \n Enter course number to edit: ")
                if course_choice == '':
                    print("Update canceled.")
                    return
                elif not course_choice.isdigit() or int(course_choice) < 1 or int(course_choice) > len(courses):
                    print("Invalid input. Please enter a valid number.")
                else:
                    break

            course_id = courses[int(course_choice) - 1][0]
            query = "SELECT * FROM courses WHERE course_id = %s"
            values = (course_id,)

            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                print("\n \n -----Current Course Information-----")
                print("Course ID:", result[0])
                print("Course Name:", result[1])

                new_code = input("Enter new code (leave empty to keep the same): ")
                new_name = input("Enter new name (leave empty to keep the same): ")
               

                if new_name or new_code:
                    update_query = "UPDATE courses SET course_name = %s, course_id = %s WHERE course_id = %s"
                    update_values = (
                        new_name if new_name else result[1],
                        new_code if new_code else result[0],
                        course_id
                    )

                    cursor.execute(update_query, update_values)
                    con.commit()
                    print("Course information updated successfully!")
                else:
                    print("No changes made to course information.")
            else:
                print("!- - - -Course not found.- - - -!")

        else:
            print("No courses found.")

        cursor.close()
    except Error as error:
        print("Error occurred while updating course information:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")

def delete_course():
    try:
        con = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='ssis123',
            database='ssis_v2'
        )

        query = "SELECT course_id, course_name FROM courses"
        cursor = con.cursor()
        cursor.execute(query)
        courses = cursor.fetchall()

        if courses:
            print("List of Courses:")
            for i, course in enumerate(courses, start=1):
                print(f"{i}.) {course[0]}, {course[1]}")

            while True:
                course_choice = input("[ press enter key to cancel ] \n \n Enter the number of the course to delete: ")
                if course_choice == '':
                    print("Deletion canceled.")
                    return
                elif not course_choice.isdigit() or int(course_choice) < 1 or int(course_choice) > len(courses):
                    print("Invalid input. Please enter a valid number.")
                else:
                    break

            course_id = courses[int(course_choice) - 1][0]
            query = "SELECT * FROM courses WHERE course_id = %s"
            values = (course_id,)

            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                print("\n \n -----Course Information-----")
                print("Course ID:", result[0])
                print("Course Name:", result[1])

                delete_query = "DELETE FROM courses WHERE course_id = %s"
                delete_values = (course_id,)

                cursor.execute(delete_query, delete_values)
                con.commit()
                print("Course deleted successfully!")
            else:
                print("!- - - -Course not found.- - - -!")

        else:
            print("No courses found.")

        cursor.close()
    except Error as error:
        print("Error occurred while deleting course:", error)
    finally:
        if con.is_connected():
            print("- - - MySQL connection closed - - -")






# Main program
print("SSIS v.2")
while True:
    print("Please choose an action: \n [ press enter key to cancel anytime ] \n \n ")
    print("----- Students -----\n" )
    print("1. Search for a student's information")
    print("2. Insert a new student record")
    print("3. Update student information")
    print("4. Delete a student")
    print("5. List all students")
    print("\n----- Courses -----\n" )
    print("6. Search for a course")
    print("7. Insert a new course")
    print("8. Update course information")
    print("9. Delete a course")
    print("10. List all courses")
    print("11. Terminate connection\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        search_student()
    elif choice == '2':
        insert_student()
    elif choice == '3':
        update_student_info()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        list_students()
    elif choice == '6':
        search_course()
    elif choice == '7':
        insert_course()
    elif choice == '8':
        update_course_info()
    elif choice == '9':
        delete_course()
    elif choice == '10':
        list_courses()    
    elif choice == '11':
        print("Terminating connection...")
        break
    else:
        print("Invalid choice!")
    print()

print("Exiting program...")
