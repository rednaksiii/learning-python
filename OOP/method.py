class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Methods in objects are functions that belong to the object
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()