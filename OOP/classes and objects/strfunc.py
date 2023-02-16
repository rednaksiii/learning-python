class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # The __str__() function controls 
  # what should be returned when the class object is represented as a string. 
  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)