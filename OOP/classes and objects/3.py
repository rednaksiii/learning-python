class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass    

lacetti = Vehicle('lacetti', 400, 400000)    

print("Vehicle name:", lacetti.name)