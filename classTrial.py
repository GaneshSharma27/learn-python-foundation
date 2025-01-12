# Making a car information app using Python classes

class CarInfo:
    def __init__(self, name, manufacturingCompany, topSpeed, fuel, seatNumber):
        self.name = name
        self.manufacturingCompany = manufacturingCompany
        self.topSpeed = topSpeed
        self.fuel = fuel
        self.seatNumber = seatNumber

    def carDict():
        
        pass
    
car1 = CarInfo(name = "BMW i5", manufacturingCompany="BMW", topSpeed="300 kmph", fuel="Diesel", seatNumber=5)
print(car1.name)