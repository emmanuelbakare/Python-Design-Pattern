class Employee:
    def __init__(self, name, position, salary):
        self.name = name 
        self.position =  position
        self.salary = salary 

    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.position
    
    def get_salary(self):
        return self.salary
    
    def __str__(self):
        return f"{self.position}: {self.name}, Salary {self.salary}"
    

class Department:
    def __init__(self, name):
        self.name  = name 
        self.children = [] 

    def add_child(self, component):
        self.children.append(component)

    def remove_child(self, component):
        self.children.remove(component)

    def get_name(self):
        return self.name 
    
    def get_employees(self):
        employees = []

        for child in self.children:
            if isinstance(child, Employee):
                employees.append(child)
            elif isinstance(child, Department):
                employees.extend(child.get_employees())

        return employees
    
    def get_total_salary(self):
        total_salary = 0

        for child in self.children:
            if isinstance(child, Employee):
                total_salary += child.get_salary()
            elif isinstance(child, Department):
                total_salary += child.get_total_salary()

        return total_salary
    
    def __str__(self):
        return f"{self.name} ( {len(self.children)} employees/department)"
    


# create some employees and departments
department1 = Department("Sales")
department1.add_child(Employee("Alice Brown", "Sales Manager", 250000))
department1.add_child(Employee("Charlie Davis", "Sales Representative", 100000))

department2 = Department("Engineering")
department2.add_child(Employee("David Lee", "Software Engineer", 150000))
department2.add_child(Employee("Eve Wang", "Software Engineer", 150000))
department2.add_child(Employee("Frank Chen", "QA Engineer", 100000))
department2.add_child(Employee("Grace Lin", "QA Engineer", 100000))
department2.add_child(Department("Infrastructure"))

department3 = Department("Marketing")
department3.add_child(Employee("Hank Kim", "Marketing Manager", 250000))
department3.add_child(Employee("Isabel Lopez", "Marketing Specialist", 100000))

ceo = Department("CEO")
employee1 = Employee("John Smith", "CEO", 1000000)
employee2 = Employee("Jane Doe", "CFO", 500000)
employee3 = Employee("Bob Johnson", "CTO", 500000)

ceo.add_child(employee1)
ceo.add_child(employee2)
ceo.add_child(employee3)

ceo.add_child(department1)
ceo.add_child(department2)
ceo.add_child(department3)

# print the employees and total salary of each department
print("Organization Chart:")
print("*"*20)
# print(f"{ceo.get_name()} ( {len(ceo.children)} employees/department), Total Salary: {ceo.get_total_salary()}")


def print_chart(department, loops=0):
    print(" "*loops,f"**{department.get_name()} ({len(department.children)}), Total Salary: {ceo.get_total_salary()}")
    
    loops += 1
    for child in department.children:
        if isinstance(child, Employee):
            print(" "*loops,child)
        elif isinstance(child, Department):
            print_chart(child, loops)
            print()


print_chart(department2)