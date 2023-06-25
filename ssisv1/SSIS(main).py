import os
import subprocess
def main():
    while True:
        print("""
        Choose an option:
        1. Student Information System
        2. Course Management System
        3. Quit
        """)

        choice = input("Enter your choice: ")

        if choice == '1':
            subprocess.call(['py', 'SSIS(student).py'])
        elif choice == '2':
            subprocess.call(['py', 'SSIS(course).py'])
        elif choice == '3':
            print("...Exiting Program. ")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()
