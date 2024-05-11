class Parent1:
    def method1(self):
        print("Method from Parent1 class")

class Parent2:
    def method2(self):
        print("Method from Parent2 class")

class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child class")

# Creating an object of the Child class
child_obj = Child()

# Accessing methods from all parent classes and child class
child_obj.method1()
child_obj.method2()
child_obj.method3()
