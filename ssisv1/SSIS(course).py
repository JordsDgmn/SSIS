import csv
import os.path
import subprocess

COURSE_FILE = 'coursedb.csv'
STUDENT_FILE = 'students.csv'


def add_course():
    with open(COURSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        course_code = input("[Press enter to cancel]\n\nEnter course code: ")
        if course_code == "":
            return
        course_name = input("[Press enter to cancel]\n\nEnter course name: ")

        if is_course_exists(course_code, course_name):
            print("Course with the same code or name already exists.")
            return

        writer.writerow([course_code, course_name])
        print("Course added successfully.")


def delete_course():
    with open(COURSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        courses = list(reader)

    if len(courses) == 0:
        print("\nDatabase is currently empty.")
        return

    print("\nCourse List:\n")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course[0]} - - - {course[1]}")

    course_num = input("[Press enter to cancel]\n\nEnter the number of the course to delete: ")
    if not course_num.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

    course_num = int(course_num)
    if not (1 <= course_num <= len(courses)):
        print("Invalid input. Please enter a valid number.")
        return

    print(f"Course to delete: {courses[course_num - 1]}")

    deleted_course_id = courses[course_num - 1][0]
    del courses[course_num - 1]

    with open(COURSE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(courses)

    clear_course_from_students(deleted_course_id)
    print("Course deleted successfully.")



def edit_course():
    with open(COURSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        courses = list(reader)

    if len(courses) == 0:
        print("There are no courses to edit.")
        return

    print("Courses:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course[0]} - {course[1]}")

    while True:
        choice = input("[Press enter to cancel]\n\nEnter the number of the course to edit: ")
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

    course_code = courses[course_index][0]

    with open(COURSE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        new_course_code = input("[Press enter to cancel]\n\nEnter new course code: ")
        new_course_name = input("[Press enter to cancel]\n\nEnter new course name: ")

        if is_course_exists(new_course_code, new_course_name):
            print("Course with the same code or name already exists.")
            return

        for i, course in enumerate(courses):
            if i == course_index:
                writer.writerow([new_course_code, new_course_name])
            else:
                writer.writerow(course)

        update_course_in_students(course_code, new_course_code, new_course_name)
        print("\nCourse edited successfully.")


def list_courses():
    if not os.path.exists(COURSE_FILE) or os.path.getsize(COURSE_FILE) == 0:
        print("The database is currently empty.\nAdd courses before trying to list them.")
        return

    with open(COURSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        courses = list(reader)

    total_courses = len(courses)
    print(f"\nTotal number of courses: {total_courses}\n")

    for course in courses:
        course_code, course_name = course
        students = get_students_by_course(course_code)
        num_students = len(students)
        print(f"Course Code: {course_code}, Course Name: {course_name}, Enrolled Students: {num_students}")

    print()


def search_course_by_name():
    while True:
        course_name = input("[Press enter to cancel]\n\nEnter course name to search: ")
        if course_name == "":
            return

        with open(COURSE_FILE, mode='r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if course_name in row[1]:
                    print("\n-- Match found! --\n")
                    print(f"Course Code: {row[0]}, Course Name: {row[1]}")
                    found = True
            if found:
                break
            else:
                print(f"\nNo course with name '{course_name}' found! Please try again.")


def search_course_by_code():
    while True:
        course_code = input("[Press enter to cancel]\n\nEnter course code to search: ")
        if course_code == "":
            return

        with open(COURSE_FILE, mode='r') as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if row[0] == course_code:
                    print("\n-- Match found! --\n")
                    print(f"Course Code: {row[0]}, Course Name: {row[1]}")
                    found = True
            if found:
                break
            else:
                print(f"\nNo course with code '{course_code}' found! Please try again.")


def is_course_exists(course_code, course_name):
    with open(COURSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == course_code or row[1] == course_name:
                return True
    return False


def clear_course_from_students(course_code):
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        students = list(reader)

    for student in students:
        if student == course_code:
            student = ""

    with open(STUDENT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)


def update_course_in_students(old_course_code, new_course_code, new_course_name):
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        students = list(reader)

    for student in students:
        if student == old_course_code:
            student = new_course_code

    with open(STUDENT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)


def get_students_by_course(course_code):
    with open(STUDENT_FILE, mode='r') as file:
        reader = csv.reader(file)
        students = list(reader)

    enrolled_students = []
    for student in students:
        if student == course_code:
            enrolled_students.append(student)

    return enrolled_students


def main():
    if not os.path.exists(COURSE_FILE):
        open(COURSE_FILE, 'w').close()

    if not os.path.exists(STUDENT_FILE):
        open(STUDENT_FILE, 'w').close()

    while True:
        print("""
        Choose an action:
        0. Go back to main menu
        1. Add a course
        2. Delete a course
        3. Edit a course
        4. List all courses
        5. Search for a course by name
        6. Search for a course by code
        7. Quit
        """)

        choice = input("Enter your choice: ")

        if choice == '0':
            os.system("python SSIS(main).py")
            break
        elif choice == '1':
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
            search_course_by_code()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
