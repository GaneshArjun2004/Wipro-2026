#Inheritance
class Vehicle:
    vehicle_count = 0   

    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")

# Single Inheritance
class Car(Vehicle):
    def start(self):
        print("Car is starting")

# Multilevel Inheritance
class ElectricCar(Car):
    def start(self):
        print("Electric Car is starting silently")

v = Vehicle()
c = Car()
e = ElectricCar()

v.start()
c.start()
e.start()
print("Total vehicles created:", Vehicle.vehicle_count)
