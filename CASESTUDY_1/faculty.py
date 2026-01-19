from person import Person
from descripter import SalaryDescriptor

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, pid, name, department, salary):
        super().__init__(pid, name, department)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("Name:", self.name)
        print("Role: Faculty")
        print("Department:", self.department)
