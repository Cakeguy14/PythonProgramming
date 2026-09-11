#TODO:

#OOP - object oriented programming

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

#TODO:

#list - mutable set of datatype object used in a function

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

#TODO:

#dict - key-value pair - when in dict you have to call the key name unlike index in list.

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

#TODO:

#class - an object reference creation for a function. you can create your own datatype.

class Student:                 
    def __init__(self, name, house):        #class is used to create a n object for us in the  memory.
        self.name = name                    #self is the attribute  used to map the instance variables into the empty object  constructed in the memory
        self.house = house                  #  __init__ function initiallizes the methods inside the class. Methods are literally the functions inside the class.

def main():
    students = get_students()
    print(f"{students.name} from {students.house}")


def get_students():
    name = input("Enter a name: ")
    house = input("Enter a house: ")
    student = Student(name, house)              #this is line is very important, as this is called Constructor object.
    return student

if __name__ == "__main__":
    main()

      
