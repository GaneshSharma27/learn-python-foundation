# ------------------- Classes and Objects -------------------
'''
1. attributes are the variables that belong to a class
2. attributes are always public and can be accessed by using the dot (.) operator
3. Example: MyClass.MyAttribute
'''

class ExampleClass:          # definition of class
    name = "XYZ"

obj = ExampleClass()         # definition of object
print(obj.name)



# ----------------------------------------------------------------------------
# creating a class
class FirstClass:
    x = 5

# creating an object
p1 = FirstClass()
print(p1.x)
print()

# The __init()__ function
class Person:
    def __init__(self, name, age):  # all classes have this function which is executed when the class is initiated 
        self.name = name
        self.age = age

    def  __str__(self):   # controls what should be returned when the class object is represented as a string
        return f"{self.name}({self.age})"
p2 = Person("Ganesh", 21)

print(p2.name)
print(p2.age)
print("Using __str()__ function:", p2)       # with using __str__() function
print()

# Object Methods - Methods in objects are functions that belong to the object
class PersonObjectMethods:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunction(self):
        print("Hello! My name is " + self.name)
personGanesh = PersonObjectMethods("Ganesh", 21)
personGanesh.myFunction()
print()

# ---------------- Class variable ----------------
# class variable are for attributes and methods share by all instances of the class
# class variable are variables whose value is assigned in the class

# -------------- Instance variable --------------
# instance variable are for data, unique to each instance
# instance variable are variables whose value is assigned inside a constructor/method with self

class Dog:
    animal = "dog"      # class variable ---> same for every instance

    def __init__(self, breed, color):
        self.breed = breed      # instance variable ---> unique to each instance
        self.color = color      # instance variable ---> unique to each instance

Tommy = Dog("pug", "brown")
Toto = Dog("bulldog", "black")

print(f"Tommy is a {Tommy.animal}")     # can also be called using `Dog.animal`
# since `animal` variable is a class variable it is going to be same for each instance of the class be it Tommy or Toto
print(f"Toto is a {Toto.animal}")       # same for Toto instance too

print(f"Breed of Tommy is {Tommy.breed}")       # instance `Tommy` has unique value for the variable
# since `breed` is an instance variable it is going to be unique for each instance of the class
print(f"Breed of Toto is {Toto.breed}")         # instance `Toto` has unique value for the variable

# Defining instance variables using the normal method
class Car:
    def __init__(self, manufacturingCompany):
        self.manufacturingCompany = manufacturingCompany
    def setCarInfo(self, model, carType, carColor, fuel):   # setting values
        self.model = model                                  # adding more instance variables
        self.carType = carType
        self.carColor = carColor
        self.fuel = fuel
    def getModel(self):                     # for retrieving the values
        return self.model
    def getCarType(self):
        return self.carType
    def getCarColor(self):
        return self.carColor
    def getFuel(self):
        return self.fuel

car1 = Car("Toyota")
car1.setCarInfo("Corola", "Sedan", "White", "Diesel")

print(f"The {car1.getModel()} is a {car1.getCarType()} which is of {car1.getCarColor()} color and runs on {car1.getFuel()}")
# `car1.manufacturingCompany()` isn't callable because
# car1.manufacturingCompany()           # will throw an error
