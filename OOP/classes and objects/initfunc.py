class Person: # class Person
  # the __init__() function to assign values to object properties  
  def __init__(self, name, age): 
    self.name = name    # properties
    self.age = age      # properties

p1 = Person("John", 36) # object

print(p1.name)
print(p1.age)