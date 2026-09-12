#TODO:

# #OOP - object oriented programming

# #tuple - a set of immutable objects used in functions.

# def main():
#     students = get_students()
#     print(f"{students[0]} from {students[1]}")


# def get_students():
#     name = input("Enter name: ")
#     house = input("Enter house: ")
#     return (name, house)

# if __name__ == "__main__":
#     main()

# #TODO:

# #list - mutable set of datatype object used in a function

# def main():
#     students = get_students()
#     if students[0] == "padma":
#         students[1] = "Ravenclaw"
#     print(f"{students[0]} from {students[1]}")


# def get_students():
#     name = input("Enter name: ")
#     house = input("Enter house: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()

# #TODO:

# #dict - key-value pair - when in dict you have to call the key name unlike index in list.

# def main():
#     students = get_students()
#     if students["name"] == "padma":
#         students["house"] = "Ravenclaw"
#     print(f"{students[0]} from {students[1]}")


# def get_students():
#     student = {}
#     student["name"] = input("Enter name: ")
#     student["house"] = input("Enter house: ")
#     return student

# #or

# def get_students():
#     name = input("Enter name: ")
#     house = input("Enter house: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()

#TODO:

#class - an object reference creation for a function. you can create your own datatype.

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

      
