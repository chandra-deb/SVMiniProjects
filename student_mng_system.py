import json
import sys
from typing import List


class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f'\n'
              f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Address: {self.address}\n'
              f'                '
              )




class Student(Person):
    def __init__(self, name: str, age: int, address: str, student_id: str, grades=None, courses_codes=None):
        super().__init__(name, age, address)
        if grades is None:
            grades = {}
        if courses_codes is None:
            courses_codes = []
        self.student_id = student_id
        self.grades = grades
        self._courses_codes = courses_codes
        self.courses = []
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id


    # CCCC
    def restore_enrolled_courses(self, all_courses):
        enrolled_courses = []
        for course in all_courses:
           if course.course_code in self._courses_codes:
               enrolled_courses.append(course)
        self.courses= enrolled_courses

    def add_grade(self, subject, grade):
        self.grades.update({subject: grade})

    def enroll_course(self, course):
        if course.course_code not in self._courses_codes:
            self._courses_codes.append(course.course_code)
            self.courses.append(course)
        else:
            pass
    def display_student_info(self):
        courses_names = ''
        for course in self.courses:
            courses_names += course.course_name + ','

        print(
            f'Student Information:\n'
            f'Name: {self.name}\n'
            f'ID: {self.student_id}\n'
            f'Age: {self.age}\n'
            f'Address: {self.address}\n'
            f'Enrolled Courses: {courses_names}\n'
            f'Grades: {self.grades}\n'
        )

    def to_json(self):

        return {
            'name': self.name,
            'id': self.student_id,
            'age': self.age,
            'address': self.address,
            'courses_codes': self._courses_codes,
            'grades': self.grades
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            name=data['name'],
            student_id=data['id'],
            age=data['age'],
            address=data['address'],
            courses_codes= data['courses_codes'],
            grades=data['grades']
        )


class Course:
    def __init__(self, course_name: str, course_code: str, instructor: str, students_ids=None):
        if students_ids is None:
            students_ids = []
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self._students_ids = students_ids
        self.students = []

    def restore_enrolled_students(self, all_students):
        students = []
        for student in all_students:
           if student.student_id in self._students_ids:
               students.append(student)
        self.students= students

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.course_code == other.course_code

    def add_student(self, student):
        if student.student_id not in self._students_ids:
            self._students_ids.append(student.student_id)
            self.students.append(student)
            print(
                f"{student.name} (ID: {student.student_id}) enrolled in {self.course_name}(Code: {self.course_code}).")
        else:
            print(f'{student.name} (ID: {student.student_id}) Already Enrolled in {self.course_name}!')

    def display_course_info(self):
        enrolled_students = ''
        for student in self.students:
            enrolled_students += student.name + ', '

        print(
            f"Course Information: \n"
            f"Course Name: {self.course_name}\n"
            f"Course Code: {self.course_code}\n"
            f"Course Instructor: {self.instructor}\n"
            f"Enrolled Students: {enrolled_students}"
        )

    def to_json(self):
        return {
            'course_name': self.course_name,
            'course_code': self.course_code,
            'instructor': self.instructor,
            'students_ids': self._students_ids,
        }

    @classmethod
    def from_json(cls, data):
        return cls(course_name=data['course_name'],
                   course_code=data['course_code'],
                   instructor=data['instructor'],
                   students_ids=data['students_ids']
                   )







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

    # Start Here
    def start(self):
        while True:
            print(
                '\n'
                '1. Add New Student\n'
                '2. Add New Course\n'
                '3. Enroll Student in Course\n'
                '4. Add Grade for Student\n'
                '5. Display Student Details\n'
                '6. Display Course Details\n'
                '7. Save Data to File\n'
                '8. Load Data from File\n'
                '0. Exit\n'
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
        address = iv.input_validate_string('Enter address: ')
        student_id = iv.input_validate_string("Enter student id: ")
        student = Student(name=name, age=age, address=address, student_id=student_id, grades={})
        if student in self.students:
            print(f'Student with ID {student_id} Already Exists in the System!')
        else:
            self.students.append(student)
            print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self):
        course_name = iv.input_validate_string('Enter Course Name: ')
        course_code = iv.input_validate_string('Enter Course Code: ')
        instructor = iv.input_validate_string('Enter Instructor: ')
        course = Course(course_name=course_name, course_code=course_code, instructor=instructor)
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
            if course in student.courses:
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
        else:
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


        self.courses = list(map(lambda c:Course.from_json(c), data['courses']))
        self.students = list(map(lambda s:Student.from_json(s), data['students']))
        for student in self.students:
            student.restore_enrolled_courses(all_courses=self.courses)
        for course in self.courses:
            course.restore_enrolled_students(all_students=self.students)

        print('Data loaded successfully.')



if __name__ == '__main__':
    StudentManagementSystem().start()
