from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Cleaning up object: {self.name}")
