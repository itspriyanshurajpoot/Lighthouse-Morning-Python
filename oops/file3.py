from abc import ABC, abstractmethod 

class Car(ABC) :
    def accelerate(self):
        print("I am accelerate function")

    @abstractmethod
    def drive(self):
        pass

class BMWCar(Car):
    def drive(self):
        print("I am drive function")

BMWCar().drive()
