
class Course:
    def __init__(self, course_name: str, course_code: str, instructor: str, students: []):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = students

    def __eq__(self, other):
        if isinstance(other, Course):
            return self.course_code == other.course_code

    def add_student(self, student ):
        if student not in self.students:
            self.students.append(student)
            print(
                f"{student.name} (ID: {student.student_id}) enrolled in {self.course_name}(Code: {self.course_code}).")
        else:
            print(f'{student.name} (ID: {student.student_id}) Already Enrolled in {self.course_name}!')

    def display_course_info(self):
        enrolled_students = ''
        for student in self.students:
            enrolled_students += student.name + ', '
        enrolled_students.rstrip(', ')

        print(f'''
Course Information: 
Course Name: {self.course_name}
sCode: {self.course_code}
sInstructor: {self.instructor}
Enrolled Students: {enrolled_students}
        ''')

    def to_json(self):
        # students = list(map(lambda student:student.to_json(), self.students))
        students = []
        for student in self.students:
            students.append(student.student_id)
        print(students)
        return {
            'course_name': self.course_name,
            'course_code': self.course_code,
            'instructor': self.instructor,
            'students': students,
        }
    @classmethod
    def from_json(cls, data):
        from student import Student
        students = list(map(lambda student:Student.from_json(student), data['students']))
        return cls(course_name=data['course_name'],
                   course_code=data['course_code'],
                   instructor=data['instructor'],
                   students= students,
                   )







