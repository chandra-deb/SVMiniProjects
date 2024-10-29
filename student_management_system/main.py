import json
import sys
from typing import List

from course import Course
from student import Student

class InputWithValidation:
    default_invalid_msg = 'Invalid Value! Try Again.'
    @classmethod
    def input_validate_string(cls, prompt='', min_length = 1, max_length=32):
        inp = input(prompt).strip()
        if min_length<=len(inp)<=max_length:
            return inp
        print(cls.default_invalid_msg)
        return cls.input_validate_string(prompt, min_length, max_length)

    @classmethod
    def input_validate_positive_int(cls, prompt='', min_int = 1, max_int=120):
        inp = input(prompt).strip().isnumeric()
        inp = int(inp)
        if min_int <= inp <= max_int:
            return inp
        print(cls.default_invalid_msg)
        return cls.input_validate_positive_int(prompt, min_int, max_int)



    @classmethod
    def input_validate_digit(cls, prompt='', exclude_digits=None):
        if exclude_digits is None:
            exclude_digits = [9]
        options = [1, 2, 3, 4, 5, 6, 7, 8,9, 0]
        for exclude_digit in exclude_digits:
            try:
                options.remove(exclude_digit)
            except ValueError:
                print('Invalid value as digit or it already got removed.')
        inp = input(prompt).strip()
        if inp.isdigit():
            inp = int(inp)
            if inp in options:
                return inp
        print(cls.default_invalid_msg)
        return cls.input_validate_digit(prompt, exclude_digits)

iv = InputWithValidation



class StudentManagementSystem:
    courses: List[Course] = []
    students: List[Student] = []


    def handle_inputs(self):
        inp = InputWithValidation.input_validate_digit('Select Option: ')
        if inp == 1:
            self.add_student()
        elif inp == 2:
            self.add_course()
        elif inp == 3:
            self.enroll_in_course()
        elif inp == 4:
            self.add_grade()
        elif inp == 5:
            self.display_student_details()
        elif inp == 6:
            self.display_course_details()
        elif inp == 7:
            self.save_data()
        elif inp == 8:
            self.load_data()
        elif inp == 0:
            print('Exiting Student Management System. Goodbye!')
            sys.exit()
        input("Press enter to continue.")

    def start(self):
        while True:
            print(
'''
1. Add New Student
2. Add New Course
3. Enroll Student in Course
4. Add Grade for Student
5. Display Student Details
6. Display Course Details
7. Save Data to File
8. Load Data from File
0. Exit
'''
            )
            self.handle_inputs()


    # CCCCC
    def get_student_by_id(self, student_id: str) -> Student | None:
        for student in self.students:
            if student.student_id == student_id:
                return student

    # CCCCC
    def get_course_by_code(self, course_code) -> Course | None:
        for course in self.courses:
            if course.course_code == course_code:
                return course

    def add_student(self):

        name = iv.input_validate_string("Enter Name: ")
        age = iv.input_validate_positive_int('Enter Age: ')
        address = iv.input_validate_string('Enter address:')
        student_id = iv.input_validate_string("Enter student id: ")
        student = Student(name=name, age=age, address=address, student_id=student_id, grades={}, courses=[])
        if student in self.students:
            print(f'Student with ID {student_id} Already Exists in the System!')
        else:
            self.students.append(student)
            print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self):
        course_name = iv.input_validate_string('Enter Course Name: ')
        course_code = iv.input_validate_string('Enter Course Code: ')
        instructor = iv.input_validate_string('Enter Instructor: ')
        course = Course(course_name=course_name, course_code=course_code, instructor=instructor, students=[])
        if course in self.courses:
            print(f'This Course with code {course_code} Already Exists in the System!')
        else:
            self.courses.append(course)
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_in_course(self):
        student_id = iv.input_validate_string('Enter Student ID: ')
        course_code = iv.input_validate_string('Enter Course Code: ')
        student = self.get_student_by_id(student_id=student_id)
        if student is not None:
            course = self.get_course_by_code(course_code=course_code)
            if course is not None:
                student.enroll_course(course=course)
                course.add_student(student=student)
            else:
                print('Enrollment Can not be done. Because this course does not exist in the System.')
        else:
            print('Enrollment Can not be done. Because this student does not exists in the System.')

    def add_grade(self):
        student_id = iv.input_validate_string('Enter Student ID: ')
        course_code = iv.input_validate_string('Enter Course Code: ')
        grade = iv.input_validate_string('Enter Grade: ')

        student = self.get_student_by_id(student_id=student_id)
        if student is not None:
            course = self.get_course_by_code(course_code=course_code)
            if course in student.get_enrolled_courses():
                student.add_grade(course.course_name, grade)
                print(f"Grade {grade} added for {student.name} in {course.course_name}.")
            else:
                print('Grade Can not be added. Because this student have not enrolled to this course or the course does not exists in the System.')
        else:
            print('Grade Can not be added. Because this student does not exists in the System.')


    def display_student_details(self):
        student_id = iv.input_validate_string('Enter Student ID: ')
        student = self.get_student_by_id(student_id=student_id)
        if student is not None:
            student.display_student_info()
        else:
            print('This student does not exists in the system.')

    def display_course_details(self):
        course_code = iv.input_validate_string('Enter course code: ')
        course = self.get_course_by_code(course_code=course_code)
        if course is not None:
            course.display_course_info()
        print('This course does not exists in the system.')

    def save_data(self):
        data = dict(courses=list(map(lambda course: course.to_json(), self.courses)),
                    students=list(map(lambda student: student.to_json(), self.students)),
                    )
        try:
            with open('data.json', 'w') as file:
                json.dump(data, file)
                print('All student and course data saved successfully.')
        except Exception as e:
            print('Error: ', e)

    def load_data(self):

        with open('data.json', 'r') as f:
            data = json.load(f)

        self.courses = list(map(lambda course:Course.from_json(course), data['courses']))
        self.students = list(map(lambda student:Student.from_json(student), data['students']))
        print('Data loaded successfully.')



if __name__ == '__main__':
    StudentManagementSystem().start()
