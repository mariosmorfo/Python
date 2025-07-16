from abc import ABC, abstractmethod

class AbstractStudentDAO(ABC):
    """Defines the student DAO API"""

    @abstractmethod
    def insert(self, student):
        pass

    @abstractmethod
    def update(self, student_id, student):
        pass

    @abstractmethod
    def delete(self, student_id):
        pass

    @abstractmethod
    def get_one(self, student_id):
        pass


class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}

    def insert(self, student):
        student_id = student["id"]
        self.students[student_id] = student
        print(f"Inserted student with ID: {student_id}")

    def update(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"Updated student with ID: {student_id}")
        else:
            print(f"Student with ID {student_id} not found")

    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Deleted student with ID: {student_id}")
        else:
            print(f"Student with ID {student_id} not found")

    def get_one(self, student_id):
        return self.students.get(student_id, None)


class ABCInventory(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item_name_to_remove):
        pass


class Inventory(ABCInventory):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added item: {item}")

    def remove_item(self, item_name_to_remove):
        for item in self.items:
            if item.name == item_name_to_remove:
                self.items.remove(item)
                print(f"Removed item: {item}")
                return
        print(f"Item not found: {item_name_to_remove}")


c
