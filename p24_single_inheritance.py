class Parent:
 
    
    def parent_method(self):
        print("This is a method from the parent class")

class Child(Parent):
   
    def child_method(self):
        print("This is a method from the child class")

# Creating an object of the Child class
child_obj = Child()

# Accessing methods from both parent and child classes
child_obj.parent_method()
child_obj.child_method()