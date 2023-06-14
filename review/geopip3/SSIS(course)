import csv
import os.path

CSV_FILE = 'coursedb.csv'


def add_course():
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        course_id = input("[ press enter key to cancel ] \n \n Enter course ID: ")
        if course_id == "":
            return
        course_name = input("[ press enter key to cancel ] \n \n Enter course name: ")
        writer.writerow([course_id, course_name])
        print("Course added successfully.")


def delete_course():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) == 0:
        print("\n \n Database is currently empty.")
        return

    print("\n Course List: \n ")
    for i, row in enumerate(rows):
        print(f"{i+1}. {row[0]} - - - {row[1]}")
    
    course_num = input("[ press enter key to cancel ] \n \n Enter the number of the course to delete: ")
    if not course_num.isdigit():
        print("Invalid input. Please enter a valid number.")
        return
    
    course_num = int(course_num)
    if not (1 <= course_num <= len(rows)):
        print("Invalid input. Please enter a valid number.")
        return

    del rows[course_num-1]
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Course deleted successfully.")




def edit_course():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        courses = list(reader)
        if len(courses) == 0:
            print("There are no courses to edit.")
            return
        print("Courses:")
        for i, course in enumerate(courses):
            print(f"{i+1}. {course[0]} - {course[1]}")
        while True:
            choice = input("[ press enter key to cancel ] \n \n Enter the number of the course to edit: ")
            if choice == "":
                return
            try:
                course_index = int(choice) - 1
                if 0 <= course_index < len(courses):
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid choice. Please enter a valid number.")
    course_id = courses[course_index][0]
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        new_course_id = input("[ press enter key to cancel ] \n \n Enter new course ID: ")
        new_course_name = input("[ press enter key to cancel ] \n \n Enter new course name: ")
        for i, course in enumerate(courses):
            if i == course_index:
                writer.writerow([new_course_id, new_course_name])
            else:
                writer.writerow(course)
        print("\n \n Course edited successfully.")



def list_courses():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        if (os.path.isfile(CSV_FILE) and os.path.getsize(CSV_FILE) > 0):
            print("\n Course List: \n ")
            for row in reader:
                print(f"{row[0]} - - - {row[1]}")
            
        else:
            print("------------------------ \n \n The database is currently empty.  \n \n Add courses before trying to list them.\n \n------------------------")
            return


def search_course_by_name():
    while True:
        course_name = input("[ press enter key to cancel ] \n \n Enter course name to search: ")
        if course_name == "":
            return
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if course_name in row[1]:
                    print("\n -- Match found! -- \n")
                    print(f"Course ID: {row[0]}, Course Name: {row[1]}")
                    found = True
            if found:
                break
            else:
                print(f"\n \n No course with name {course_name} found! Please try again. ")


def search_course_by_id():
    while True:
        course_id = input("[ press enter key to cancel ] \n \n Enter course ID to search: ")
        if course_id == "":
            return
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if row[0] == course_id:
                    print("\n -- Match found! -- \n")
                    print(f"Course ID: {row[0]}, Course Name: {row[1]}")
                    found = True
            if found:
                break
            else:
                print(f"\n \n No course with ID {course_id} found! Please try again.")



if not os.path.exists(CSV_FILE):
    open(CSV_FILE, 'w').close()

while True:
    print("""
    Choose an action:
    1. Add a course
    2. Delete a course
    3. Edit a course
    4. List all courses
    5. Search for a course by name
    6. Search for a course by ID
    7. Quit
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        add_course()
    elif choice == '2':
        delete_course()
    elif choice == '3':
        edit_course()
    elif choice == '4':
        list_courses()
    elif choice == '5':
        search_course_by_name()
    elif choice == '6':
        search_course_by_id()
    elif choice == '7':
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")

