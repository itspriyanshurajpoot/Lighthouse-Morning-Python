# Create class
class Human :
    # def giveValue(self, name, gender, age, bloodGroup):
    #     self.name = name
    #     self.gender = gender
    #     self.age = age
    #     self.bloodGroup = bloodGroup

    def __init__(self, name, gender, age, bloodGroup):
            self.__name = name
            self.gender = gender
            self.__age = age
            self.__bloodGroup = bloodGroup
            print("I am parent class constructor")

    def getName(self):
         return self.__name

    def getAge(self):
        return self.__age

    def getBloodGroup(self):
        return self.__bloodGroup
    
    def setName(self, name):
         self.__name = name

    def __str__(self):
        return f"Name is {self.__name}, age is {self.__age}, gender is {self.gender} and bloodGroup is {self.__bloodGroup}"

    def __del__(self):
        print("I am a destructor")


# rajesh = Human("Rajesh", 'M', 20, 'A+')
# # rajesh.displayValue()
# print(rajesh)
# rajesh.gender = 'Male'
# print(rajesh.gender)
# rajesh.setName("Raj")
# print(rajesh.getName())


# sehbaj = Human("Sehbaz", 'M', 20, 'A+')
# # sehbaj.displayValue()
# print(sehbaj)