from person import Person
from descripter import MarksDescriptor
from decorators import log_execution, execution_time

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, pid, name, department, semester, marks):
        super().__init__(pid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def get_details(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Role: Student")
        print("Department:", self.department)

    @log_execution
    @execution_time
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B"
        print("Average:", round(avg, 2))
        print("Grade:", grade)
        return avg

    def __gt__(self, other):
        return self.calculate_performance() > other.calculate_performance()
