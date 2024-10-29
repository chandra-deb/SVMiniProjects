from typing import List
from person import Person


class Student(Person):
    def __init__(self, name: str, age: int, address: str, student_id: str, grades: dict, courses: []):
        super().__init__(name, age, address)
        # self.student_id = Student._count_id + 1
        self.student_id = student_id
        self.grades = grades
        self.courses = courses
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id


    # CCCC
    def get_enrolled_courses(self) -> []:
        return self.courses

    def add_grade(self, subject, grade):
        self.grades.update({subject: grade})

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            pass
    def display_student_info(self):
        enrolled_courses = ''
        for course in self.get_enrolled_courses():
            enrolled_courses += course.course_name + ', '
        print(
            f'''
Student Information:
Name: {self.name}
ID: {self.student_id}
Age: {self.age}
Address: {self.address}
Enrolled Courses: {enrolled_courses}
Grades: {self.grades}
'''
        )

    def to_json(self):
        # courses = list(map(lambda course: course.to_json(), self.courses))
        courses = []
        for course in self.courses:
            courses.append(course.course_code)
        return {
            'name': self.name,
            'id': self.student_id,
            'age': self.age,
            'address': self.address,
            'courses': courses,
            'grades': self.grades

        }

    @classmethod
    def from_json(cls, data):
        from course import Course
        courses = list(map(lambda course:Course.from_json(course), data['courses']))

        return cls(
            name=data['name'],
            student_id=data['id'],
            age=data['age'],
            address=data['address'],
            courses= courses,
            grades=data['grades']
        )

