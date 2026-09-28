'''
Task: Build a basic management system of your own choice such as student, online shop etc, that uses the idea of inheritance.
Also, mention the type of inheritance being used.
'''
#----In this program Hybrid Inheritance is used----
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}\n Employee ID: {self.employee_id}\n Salary: {self.salary}")


class Project:
    def __init__(self, project_name):
        self.project_name = project_name

    def display_project(self):
        print("Project Name: ", self.project_name, "\n")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Department: ", self.department, "\n")


class Engineer(Employee, Project):
    def __init__(self, name, employee_id, salary, project_name):
        Employee.__init__(self, name, employee_id, salary)
        Project.__init__(self, project_name)

    def display_info(self):
        super().display_info()
        self.display_project()


class SupportStaff(Employee):
    def __init__(self, name, employee_id, salary, role):
        super().__init__(name, employee_id, salary)
        self.role = role

    def display_info(self):
        super().display_info()
        print("Role: ", self.role, "\n")


# Creating objects of the classes
manager = Manager("Luffy", "A-123", 80000, "HR")
manager2 = Manager("Zoro", "S-456", 85000, "Sales")
engineer = Engineer("Sanji", "E-789", 60000, "Project-X")
engineer2 = Engineer("Shanks", "E-111", 62000, "Project-Y")
support_staff = SupportStaff("Gojo", "SS-486", 40000, "Admin")
support_staff2 = SupportStaff("Kira", "SS-153", 42000, "Receptionist")

# Displaying information
print("Manager Information:")
manager.display_info()
manager2.display_info()

print("\nEngineer Information:")
engineer.display_info()
engineer2.display_info()

print("\nSupport Staff Information:")
support_staff.display_info()
support_staff2.display_info()


