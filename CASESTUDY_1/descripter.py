class MarksDescriptor:
    def __get__(self, obj, owner):
        return obj._marks

    def __set__(self, obj, value):
        if all(0 <= m <= 100 for m in value):
            obj._marks = value
        else:
            raise ValueError("Marks should be between 0 and 100")

class SalaryDescriptor:
    def __get__(self, obj, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        obj._salary = value
