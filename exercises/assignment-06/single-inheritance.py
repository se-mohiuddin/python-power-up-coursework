'''
Task: Build a basic management system of your own choice such as student, online shop etc, that uses the idea of inheritance.
Also, mention the type of inheritance being used.
'''
#----It this program single inheritance is used----
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


class Student(Person):
    def __init__(self, name, age, roll_number, grade):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.grade = grade

    def display_info(self):
        super().display_info()
        print("Roll Number: ", self.roll_number)
        print("Grade: ", self.grade, "\n")


class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def display_info(self):
        super().display_info()
        print("Employee ID: ", self.employee_id)
        print("Subject: ", self.subject, "\n")


# Creating objects of the classes
student1 = Student("Alice", 18, "S123", "10th")
teacher1 = Teacher("Mr. Smith", 35, "T456", "Mathematics")

# Displaying information
print("Student Information:")
student1.display_info()
print("\nTeacher Information:")
teacher1.display_info()
