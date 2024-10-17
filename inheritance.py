class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling the method to display information
person1.display_info()  # Output: Name: Alice, Age: 30
person2.display_info()  # Output: Name: Bob, Age: 25
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

# Creating objects of the Student class
student1 = Student("Carol", 22, "12345")
student2 = Student("David", 20, "54321")

# Calling the method to display information
student1.display_info()  # Output: Name: Carol, Age: 22, Student ID: 12345
student2.display_info()  # Output: Name: David, Age: 20, Student ID: 54321
