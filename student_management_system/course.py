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
