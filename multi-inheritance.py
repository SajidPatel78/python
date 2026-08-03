# Base class
class base:
    def __init__(self, name, roll, role):
        self.name = name
        self.roll = roll
        self.role = role
    

# Intermediate class
class intermidiate(base):
    def __init__(self, name, roll, role, age):
        super().__init__(name, roll, role)
        self.age = age


# Derived class
class derived(intermidiate):
    def __init__(self, name, roll, role, age, gender):
        super().__init__(name, roll, role, age)
        self.gender = gender

    def printdata(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Role:", self.role)
        print("Age:", self.age)
        print("Gender:", self.gender)


# Creating object
obj = derived("Sajid", "21", "Student", 20, "Male")

# Printing data
obj.printdata()