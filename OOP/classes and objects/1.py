# Write a Python program to create a Vehicle class 
# with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

lacetti = Vehicle(300, 300000)

print("Max speed of lacetti:", lacetti.max_speed ,"\nMileage:", lacetti.mileage)

