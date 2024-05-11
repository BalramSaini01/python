class Grandparent:
     def grandparent_method(self):
        print("This is a method from the Grandparent class")

class Parent(Grandparent):
   def parent_method(self):
        print("This is a method from the Parent class")

class Child(Parent):
  def child_method(self):
        print("This is a method from the Child class")

# Creating an object of the Child class
child_obj = Child()

# Accessing methods from all three classes
child_obj.grandparent_method()
child_obj.parent_method()
child_obj.child_method()
