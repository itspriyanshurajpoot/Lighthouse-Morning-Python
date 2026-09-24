from file1 import Human  

class Student(Human) :
    collegeName = "ABC"

    def __init__(self, name, gender, age, bloodGroup, rollNo, courses):
        super().__init__(name, gender, age, bloodGroup)
        self.rollNo = rollNo
        self.courses = courses
        print("I am child class constructor")

    @classmethod
    def initializeCollegeName(cls, name):
        cls.collegeName = name


    def sayHello():
        print("I am instance function")

    def __del__(self):
        print(" I am child class destructor")

    

    def __str__(self):
        return f"Name is {self.getName()}, age is {self.getAge()}, gender is {self.gender}, bloodGroup is {self.getBloodGroup()}, rollNo : {self.rollNo} and cources are {self.courses}"


# omkar = Student("Omkar", 'M', 20, 'A+', 101, ['SQL', 'Python'])
# print(omkar)

Student.initializeCollegeName("MNO")
print(Student.collegeName)

Student.sayHello()

# krushil = Student("Krushil", 'M', 20, 'A+', 101, ['SQL', 'Python'])
# print(krushil.collegeName)
