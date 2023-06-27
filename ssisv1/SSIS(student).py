import csv
import os.path
import os

STUDENT_FILE = 'students.csv'


def add_student():
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        students = list(reader)

    existing_ids = [student[0] for student in students]

    while True:
        student_id = input("[ press enter key to cancel ] \n \n Enter Student ID: ")
        if student_id == "":
            return
        elif student_id in existing_ids:
            print("Student ID already exists. Please enter a unique ID.")
        else:
            break

    student_name = input("[ press enter key to cancel ] \n \n Enter student name: ")
    course_code = input("[ press enter key to cancel ] \n \n Enter course code: ")

    with open(STUDENT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_id, student_name, course_code])
    print("\n \n Student added successfully.")


def delete_student():
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        students = list(reader)

    if not students:
        print("No students found.")
        return

    print("List of students:")
    for i, student in enumerate(students):
        print(f"{i+1}. {student}")

    while True:
        selection = input("[ press enter key to cancel ] \n \n Enter the number of the student to delete: ")
        if selection == "":
            return

        try:
            selection = int(selection)
            if selection < 1 or selection > len(students):
                raise ValueError()
            break
        except ValueError:
            print("Invalid selection. Please enter a number between 1 and", len(students))

    student_id = students[selection - 1][0]
    rows = [row for row in students if row[0] != student_id]
    with open(STUDENT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Student deleted successfully.")


def edit_student():
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        students = list(reader)

    if len(students) == 0:
        print("There are no students to edit.")
        return

    print("Students:")
    for i, student in enumerate(students):
        print(f"{i + 1}. {student}")

    while True:
        choice = input("[ press enter key to cancel ] \n \n Enter the number of the student to edit: ")
        if choice == "":
            return
        try:
            student_index = int(choice) - 1
            if 0 <= student_index < len(students):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid choice. Please enter a valid number.")

    student_id = students[student_index][0]
    with open(STUDENT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for i, student in enumerate(students):
            if i == student_index:
                new_student_id = input("[ press enter key to cancel ] \n \n Enter new student ID: ")
                new_student_name = input("[ press enter key to cancel ] \n \n Enter new student name: ")
                new_course_code = input("[ press enter key to cancel ] \n \n Enter new course code: ")
                writer.writerow([new_student_id, new_student_name, new_course_code])
            else:
                writer.writerow(student)
        print("\n \n Student edited successfully.")




def list_students():
    if not os.path.exists(STUDENT_FILE) or os.path.getsize(STUDENT_FILE) == 0:
        print("------------------------ \n \n The database is currently empty.  \n \n Add students before trying to list them.\n \n------------------------")
        return
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:
                print(f"{i+1}. {row[0]}, {row[1]}, {row[2]}")


def search_student_by_name():
    student_name = input("[ press enter key to cancel ] \n \n Enter student name to search: ")
    if student_name == "":
        return
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        found = False
        count = 0
        for row in reader:
            if len(row) >= 3 and student_name in row[1]:
                if not found:
                    print("\n -- Matches found! -- \n")
                print(f"Student ID: {row[0]}, Student Name: {row[1]}, Course Code: {row[2]}")
                found = True
                count += 1
        if not found:
            print(f"\n \n No student with name {student_name} found!")
        else:
            print(f"\n \n Total matches found: {count}")


def search_student_by_id():
    student_id = input("[ press enter key to cancel ] \n \n Enter student ID to search: ")
    if student_id == "":
        return
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        found = False
        count = 0
        for row in reader:
            if len(row) >= 3 and row[0] == student_id:
                if not found:
                    print("\n -- Matches found! -- \n")
                print(f"Student ID: {row[0]}, Student Name: {row[1]}, Course Code: {row[2]}")
                found = True
                count += 1
        if not found:
            print(f"\n \n No student with ID {student_id} found!")
        else:
            print(f"\n \n Total matches found: {count}")


def search_student_by_course():
    course_code = input("[ press enter key to cancel ] \n \n Enter course code to search: ")
    if course_code == "":
        return
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        found = False
        count = 0
        for row in reader:
            if len(row) >= 3 and row[2] == course_code:
                if not found:
                    print("\n -- Matches found! -- \n")
                print(f"Student ID: {row[0]}, Student Name: {row[1]}, Course Code: {row[2]}")
                found = True
                count += 1
        if not found:
            print(f"\n \n No student with course code {course_code} found!")
        else:
            print(f"\n \n Total matches found: {count}")


if not os.path.exists(STUDENT_FILE):
    open(STUDENT_FILE, 'w').close()

while True:
    print("""
    Choose an action:
    0. Go back to main menu
    1. Add a student
    2. Delete a student
    3. Edit a student
    4. List all students
    5. Search for a student by name
    6. Search for a student by ID
    7. Search for students by course code
    8. Quit
    """)

    choice = input("Enter your choice: ")

    if choice == '0':
        import os
        os.system('python SSIS(main).py')
        break
    elif choice == '1':
        add_student()
    elif choice == '2':
        delete_student()
    elif choice == '3':
        edit_student()
    elif choice == '4':
        list_students()
    elif choice == '5':
        search_student_by_name()
    elif choice == '6':
        search_student_by_id()
    elif choice == '7':
        search_student_by_course()
    elif choice == '8':
        print("...Exiting Program")
        break
    else:
        print("Invalid choice, please try again.")
