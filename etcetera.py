#TODO:
#set - unordered, mutable, non-hashable, non-indexable, NO DUPLICATES

# students = [{"name": "harry", "house": "gryfindor"}, {"name": "hermoine", "house": "slytherin"}]

# # houses = []

# # for student in students:
# #     if student["house"] not in houses:
# #         houses.append(student["house"])

# # for house in houses:
# #     print(house)

# houses = set()                 #set uses add instead of append like list

# for student in students:
#     if student["house"] not in houses:
#         houses.add(student["house"])

# for house in sorted(houses):
#     print(house)

#TODO:

#gobal variables

# balance = 0 

# def main():
#     print("balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("balance:", balance)

# def deposit(amount):
#     global balance      # if a variable is defined inside main function or any function that has been then its fine, TODO: BUT!
#     balance += amount

# def withdraw(amount):   # BUT! if a variable is defined outside of functions i.e, global. to call it in function use TODO: global variable
#     global balance
#     balance -= amount

# if __name__ == "__main__":
#     main()

#TODO: best option is to write inside a class for these kind of functions. As they are related

class Bank:
    def __init__(self):
        amount = int(input("Enter a value: "))
        self.balance = amount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("not allowed")
        self._balance = amount

    def withdraw(self, amount):
        if amount < self._balance:
            self.balance -= amount

    def __str__(self):
        return f"{self.balance} is your balance"

def main():
    account = Bank()
    print(account.balance)
    # account.deposit(100)
    account.withdraw(50)
    print(account.balance)

if __name__ == "__main__":
    main()

#TODO:

#constants - when you have value/integer/anything thats going to stay constant over time. you can use Class Constants

class Cat:
    MEOWS = 3

    def meows(self):
        for _ in range(Cat.MEOWS):    #Cat.MEOWS is the constant here. Its going to be called via methods and stay the same.
            print("Meow")

cat = Cat()
cat.meows()

#TODO:

#type hints

def meow(n: int) -> None:             #adding n: int defines type hinting that input should be int
    for _ in range(n):
        print("meow")

num: int = int(input("enter a num: "))   #main purpose of typw hinting to to identify any type error in code using mypy lib
meow(num)

#or

def meow(n: int) -> str:             #adding n: int defines type hinting that input should be int
    return "mewo\n" * n

num: int = int(input("enter a num: "))   #main purpose of typw hinting to to identify any type error in code using mypy lib
meow(num)

#TODO:

#docstrings - documenting kind of markdown language

def meow(n: int) -> str:             #adding n: int defines type hinting that input should be int
    """
    Meow n time when called
    :param n: number of times
    :type of n: int
    :raise typeerror: If n is not a int
    :return type: str
    """
    return "mewo\n" * n

num: int = int(input("enter a num: "))   #main purpose of typw hinting to to identify any type error in code using mypy lib
meow(num)

#TODO:

#command line n numberinput using sys lib

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and (sys.argv[1]) == "-n":
    num = int(sys.argv[2])
    for _ in range(num):
        print("meow")
else:
    print("not correct syntax")


