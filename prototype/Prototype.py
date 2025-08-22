import copy


class Student:
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, University: {self.university}"

    def clone(self):
        return copy.deepcopy(self)


original_student = Student("Ali", 20, "TUIT")
student_copy = original_student.clone()
student_copy.name = "Vali"
print("Original Student ---", original_student)
print("Student copied ---", student_copy)
