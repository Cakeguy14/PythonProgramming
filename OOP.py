#TODO:

# #OOP - object oriented programming

#tuple - a set of immutable objects used in functions.

def main():
    students = get_students()
    print(f"{students[0]} from {students[1]}")


def get_students():
    name = input("Enter name: ")
    house = input("Enter house: ")
    return (name, house)

if __name__ == "__main__":
    main()

# #TODO:

# #list - mutable set of datatype object used in a function

def main():
    students = get_students()
    if students[0] == "padma":
        students[1] = "Ravenclaw"
    print(f"{students[0]} from {students[1]}")


def get_students():
    name = input("Enter name: ")
    house = input("Enter house: ")
    return [name, house]

if __name__ == "__main__":
    main()

# #TODO:

# #dict - key-value pair - when in dict you have to call the key name unlike index in list.

def main():
    students = get_students()
    if students["name"] == "padma":
        students["house"] = "Ravenclaw"
    print(f"{students[0]} from {students[1]}")


def get_students():
    student = {}
    student["name"] = input("Enter name: ")
    student["house"] = input("Enter house: ")
    return student

#or

def get_students():
    name = input("Enter name: ")
    house = input("Enter house: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()

# #TODO:

# #class - an object reference creation for a function. you can create your own datatype.

class Student:                 
    value_house = ["Gryfindor","Slyhterin", "Hufflepuff", "Ravenclaw"]
    def __init__(self, name, house, patronus):        #class is used to create a n object for us in the  memory.
        if not name:
            raise ValueError("Give a Name")
        if house.lower() not in self.value_house:
            raise ValueError("You are a muggle son!")
        self.name = name                              #self is the attribute  used to map the instance variables into the empty object  constructed in the memory
        self.house = house                            #  __init__ function initiallizes the methods inside the class. Methods are literally the functions inside the class.
        self.patronus = patronus

    def __str__(self):                                # __str__ method helps the attribute to be printed as string instead of the memory details of the object where the attribute is.
        return print(f"{self.name} from {self.house}")

    def charm(self):
        match self.patronus:                          #Use self.patronus why because the charm function is within the class itself. since the patronus is already existing inside the __init__ func. 
            case "stag":                              #No need to give it(patronus)/(parameter) one more time. Thats a redundant design.
                return "🦌 A deer-like picture appears!"
            case "otter":
                return "🦦 A playful otter appears!"
            case _:
                return "✨ A mysterious shape appears!"

#or

    def charm(self):
        if self.patronus == "wolf":
            return "🐺 A fierce wolf appears!"

    @property                                        #TODO: when a validation step is required in any class and TODO: also prevent the outside of class user given values/hardcoding outside class.
    def house(self):
        return self._house                           #TODO: Getter will called when reading happens in print statement. Always use _variable/_attribute.

    @house.setter
    def house(self, house):
        if house.lower() not in self.value_house:    #TODO: its used when writing happens from input value. goes through validations and send data into object to show.
            raise ValueError("wrong house")
        self._house = house

def main():
    students = get_students()                         #every time when a attribute from object is called outside of class. use the classname.attribute.
    print(f"{students.name} from {students.house}")   #because if function within class you can easily say self.attribute
    students.house = "HOUSE"                          #TODO: this is exactly what we are trying to prevent in line-99.
    print(Student.charm())                            #its not always necessary to return in main like other func, because in main we'll mostly just print the end results.


def get_students():
    name = input("Enter a name: ")
    house = input("Enter a house: ")
    patronus = input("Enter your charm: ")
    student = Student(name, house, patronus)              #this is line is very important, as this is called Constructor object.
    return student                         #you have to return the variable which got the input stored. otherwise it'll not make sense because the a function of a function is return a value when called/used

if __name__ == "__main__":
    main()

      
#TODO:
#@classmethod helps you to create a method inside class that allows you to not explicitly initiate/construct the class object into a variable when called externally. that step can be skipped.

import random
class Hat:
    #def __init__(self):                                                         #TODO:when cls in classmethods is introduced no need to use self anywhere
        #self.houses = ["Gryfindor","Slyhterin", "Hufflepuff", "Ravenclaw"]

    houses = ["Gryfindor","Slyhterin", "Hufflepuff", "Ravenclaw"]

    @classmethod            #when class method is added, TODO: you need to be careful and always use cls instead of self. because class method replaces instance method with class method as name suggests
    def sort(cls, name):
        #house = random.choice(cls.houses)
        print(name, "is in", random.choice(cls.houses)) #or house)

#hat = Hat()                 #Also, this line is not needed once class method is introduced. you can straight use class.method("variable name") option.TODO: No need to construct the class to a variable.                
Hat.sort("harry")

# #TODO:

# #moving the get_student() funtion into a class and make it a method/function.

class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return (f"{self.name} is in {self.house}")

    @classmethod
    def get(cls):
        name = input("Enter the name: ")
        house = input("Enter the house: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

#TODO:

#Inheritence - Parent class to child class. if they share similar trait and incase have to inherit some method from parent to child.

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("missing name")
        self.name = name

    def __str__(self):
        return (self.name)

class Student(Wizard):
    def __init__(self, name, patronus):
        super().__init__(name)
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} has a {self.patronus} as patronus"

class Professor(Wizard):
    def __init__(self, name, patronus):
        super().__init__(name)
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} has a {self.patronus} as patronus"

def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Stag")
    professor = Professor("Snape", "Deer")
    print(wizard)
    print(student)
    print(professor)

if __name__ == "__main__":
    main()


#TODO:

#operator overloading - when we want to add or do any arthmetic functions outside the class using methods from the class for an
#                       instance variable. this function is helpful for that.

class Coins:
    def __init__(self, thousands, hundreds, tens):
        self.thousands = thousands
        self.hundreds = hundreds
        self.tens = tens

    def __str__(self):
        return f"{self.thousands}, {self.hundreds}, {self.tens}"

    def __add__(self, other):
        thousands = self.thousands + other.thousands
        hundreds = self.hundreds + other.hundreds
        tens = self.tens + other.tens
        return Coins(thousands=thousands, hundreds=hundreds, tens=tens) # you can easily manipulate the position and confuse the class/python
                                                                        # always give as keyword arguments i.e, thousands=thousands etc

potter = Coins(100, 50, 25)
ron = Coins(50, 25, 25)

total = potter + ron

print(total)
print(potter)
print(ron)

# thousand = potter.thousands + ron.thousands       # this is also right, but not optimal.
# hundred = potter.hundreds + ron.hundreds
# ten = potter.tens + ron.tens

# print(thousands, hundreds, ten)