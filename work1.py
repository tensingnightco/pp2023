import sys

students = {} 
courses = {}
marks = {}

def students_data():
    num_students = int(input("Enter the number of students in the class: "))
    for i in range (num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student's date of birth: ")
        students[student_id] = {'name': student_name, 'dob': student_dob}

def courses_data():
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course_id = input("Enter the course ID: ")
        course_name = input("Enter the course name: ")
        courses[course_id] = {'name': course_name}


def marks_data():
    course_id = input("Enter the courses ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return 
    for student_id in students:
        mark = int(input(f"Enter the mark for {students[student_id]['name']}: "))
        if student_id not in marks:
          marks[student_id] = {}
        marks[student_id][course_id] = mark

def list_courses():
    for course_id in courses:
        print(f"{course_id}: {courses[course_id]['name']}")

def list_students():
    for student_id in students:
        print(f"{student_id}: {students[student_id]['name']}")

def show_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for student_id in students:
        if student_id in marks and course_id in marks[student_id]:
            print(f"{students[student_id]['name']}: {marks[student_id][course_id]}")
        else:
            print(f"{students[student_id]['name']}: N/A")

def print_invalid():
    print("Invalid choice")

students_data()
courses_data()

while True:
    print("Select an option:")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given course")
    print("5. Quit")
    try:
        choice = int(input("Enter your choice: "))
        choices = {
            1: marks_data,
            2: list_courses,
            3: list_students,
            4: show_marks,
            5: sys.exit,
        }
        func = choices[choice]
        func()
    except KeyError:
        print_invalid()
    except TypeError:
        print_invalid()

