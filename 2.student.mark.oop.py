import sys

## Define class

class Grades:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

class Student(Grades):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name)
        self.__dob = dob

## Add polymorphism in source code
    
    def get_dob(self):
        return self.__dob
    
    def set_dob(self, dob):
        self.__dob = dob

class Course(Grades):
    def __init__(self, course_id, name):
        super().__init__(course_id, name)

## Polymorphism

class Mark:
    def __init__(self, mark):
        self.__mark = mark
    
    def get_mark(self):
        return self.__mark

class GPA:
    def __init__(self):
        self.__students = {}
        self.__courses = {}
        self.__marks = {}
## Student input
    def add_student(self):
        num_students = int(input("Enter the number of students in the class: "))
        for i in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student's date of birth: ")
            student = Student(student_id, student_name, student_dob)
            self.__students[student_id] = student
## Course input
    def add_course(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            course_id = input("Enter the course ID: ")
            course_name = input("Enter the course name: ")
            course = Course(course_id, course_name)
            self.__courses[course_id] = course

## Add marks for specified course
    def add_marks(self):
        course_id = input("Enter the courses ID: ")
        if course_id not in self.__courses:
            print("Invalid course ID")
            return
        for student_id, student in self.__students.items():
            mark = int(input(f"Enter the mark for {student.get_name()}: "))
            if student_id not in self.__marks:
                self.__marks[student_id] = {}
            mark = Mark(mark)
            self.__marks[student_id][course_id] = mark
## List all the courses defined when choosing option 2

    def list_courses(self):
        for course_id, course in self.__courses.items():
            print(f"{course.get_id()}: {course.get_name()}")
## List all the students defined when choosing option 3

    def list_students(self):
        for student_id, student in self.__students.items():
            print(f"{student.get_id()}: {student.get_name()}")
## Option 4

    def show_marks(self):
        course_id = input("Enter the course ID: ")
        if course_id not in self.__courses:
            print("Invalid course ID")
            return
        for student_id, student in self.__students.items():
            if student_id in self.__marks and course_id in self.__marks[student_id]:
                mark = self.__marks[student_id][course_id].get_mark()
                print(f"{student.get_name()}: {mark}")
            else:
                print(f"{student.get_name()}: N/A")

    def print_invalid(self):
        print("Invalid choice")

    def run(self):
        self.add_student()
        self.add_course()

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
                    1: self.add_marks,
                    2: self.list_courses,
                    3: self.list_students,
                    4: self.show_marks,
                    5: sys.exit,
                }
                func = choices[choice]
                func()
            except KeyError:
                self.print_invalid()
            except TypeError:
                self.print_invalid()

if __name__ == "__main__":
    gpa = GPA()
    gpa.run()
