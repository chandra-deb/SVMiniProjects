from person import Person


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



