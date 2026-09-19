# TODO:
# set - unordered, mutable, non-hashable, non-indexable, NO DUPLICATES

# students = [{"name": "harry", "house": "gryfindor"}, {"name": "hermoine", "house": "slytherin"}]

# # houses = []

# # # for student in students:
# # #     if student["house"] not in houses:
# # #         houses.append(student["house"])

# # # for house in houses:
# # #     print(house)

# # houses = set()                 #set uses add instead of append like list

# # for student in students:
# #     if student["house"] not in houses:
# #         houses.add(student["house"])

# # for house in sorted(houses):
# #     print(house)

# #TODO:

# #gobal variables

# # balance = 0

# # def main():
# #     print("balance:", balance)
# #     deposit(100)
# #     withdraw(50)
# #     print("balance:", balance)

# # def deposit(amount):
# #     global balance      # if a variable is defined inside main function or any function that has been then its fine, TODO: BUT!
# #     balance += amount

# # def withdraw(amount):   # BUT! if a variable is defined outside of functions i.e, global. to call it in function use TODO: global variable
# #     global balance
# #     balance -= amount

# # if __name__ == "__main__":
# #     main()

# #TODO: best option is to write inside a class for these kind of functions. As they are related

# class Bank:
#     def __init__(self):
#         amount = int(input("Enter a value: "))
#         self.balance = amount

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             raise ValueError("not allowed")
#         self._balance = amount

#     def withdraw(self, amount):
#         if amount < self._balance:
#             self.balance -= amount

#     def __str__(self):
#         return f"{self.balance} is your balance"

# def main():
#     account = Bank()
#     print(account.balance)
#     # account.deposit(100)
#     account.withdraw(50)
#     print(account.balance)

# if __name__ == "__main__":
#     main()

# #TODO:

# #constants - when you have value/integer/anything thats going to stay constant over time. you can use Class Constants

# class Cat:
#     MEOWS = 3

#     def meows(self):
#         for _ in range(Cat.MEOWS):    #Cat.MEOWS is the constant here. Its going to be called via methods and stay the same.
#             print("Meow")

# cat = Cat()
# cat.meows()

# #TODO:

# #type hints

# def meow(n: int) -> None:             #adding n: int defines type hinting that input should be int
#     for _ in range(n):
#         print("meow")

# num: int = int(input("enter a num: "))   #main purpose of typw hinting to to identify any type error in code using mypy lib
# meow(num)

# #or

# def meow(n: int) -> str:             #adding n: int defines type hinting that input should be int
#     return "mewo\n" * n

# num: int = int(input("enter a num: "))   #main purpose of typw hinting to to identify any type error in code using mypy lib
# meow(num)

# #TODO:

# #docstrings - documenting kind of markdown language

# def meow(n: int) -> str:             #adding n: int defines type hinting that input should be int
#     """
#     Meow n time when called
#     :param n: number of times
#     :type of n: int
#     :raise typeerror: If n is not a int
#     :return type: str
#     """
#     return "mewo\n" * n

# num: int = int(input("enter a num: "))   #main purpose of typw hinting to to identify any type error in code using mypy lib
# meow(num)

# #TODO:

# #command line n numberinput using sys lib

# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and (sys.argv[1]) == "-n":
#     num = int(sys.argv[2])
#     for _ in range(num):
#         print("meow")
# else:
#     print("not correct syntax")

# TODO:

# arg parser - to automate the arg parsing in a python file giving input to run

# import argparse

# parser = argparse.ArgumentParser(description="meow like a cat)
# parser.add_argument("-n", default=1, help="this program is to meow like a cat", type=int)
# arg = parser.parse_args()

# for _ in range(arg.n):
#     print("meow")


# #TODO:

# #unpacking

# def total(galleons, sickles, knuts):
#     return(galleons * 5 + sickles * 2) * knuts

# coins = [100,50,25]

# print(f"{total(*coins)} knuts")   # * - helps the list to unpack and assign each coins values to the parameter into the functions. #TODO: precursor of *args - tuple,list

# #or

# def total(galleons, sickles, knuts):
#     return(galleons * 5 + sickles * 2) * knuts

# print(total(galleons=100,sickles=50,knuts=25), "knuts")   #you can also use keyword= arguments method to pass arguments to the function.

# #or

# def total(galleons, sickles, knuts):
#     return(galleons * 5 + sickles * 2) * knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(f"{total(**coins)} knuts")    #TODO: precursor of **kwargs - dict


# #TODO:

# #*args, **kwargs

# def main():
#     yell(["this", "is", "cs50"])


# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)                    # *args - *uppercased helps you to unpack the result list into individual values/strings.

# if __name__ == "__main__":
#     main()

# #or

# def main():
#     yell("this", "is", "cs50")


# def yell(*words):                        # if not list passed in and a value/string is passed. then you have pass the value via *arg parameter inside the function.
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__ == "__main__":
#     main()


# #or TODO: using map function we can get rid of the loop and use it as it is.

# def main():
#     yell("this", "is", "cs50")


# def yell(*words):
#     uppercased = map(str.upper, words)  # map function helps to go through each argument passed and helps to achieve the given function
#     print(*uppercased)                  # map() returns an iterator, not a list. Iterators can only be consumed once.
#                                         # map() call all the items passed into it, filter() calls only particular passes criteria.
# if __name__ == "__main__":
#     main()

# TODO:

# list comprehension

# students = [{"name": "harry", "house": "gryfindor"}, {"name": "hermoine", "house": "slytherin"}]

# Student = [student["name"] for student in students if student["house"] == "gryfindor"]

# for _ in Student:
#     print(_)

# or TODO: filter function also similar to map function only difference is that the map will to the arg passing for in a given list/input. filter only do for functions specified filter.

# students = [
#     {"name": "harry", "house": "gryfindor"},
#     {"name": "hermoine", "house": "slytherin"},
# ]


# def is_gryfindor(s):
#     return s["house"] == "gryfindor"                   #TODO: important note is that, here S is just a placeholder you can use any name/character here.


# gryfindors = filter(is_gryfindor, students)                   #TODO: since, we are originally calling the students variable itself here. the filter function knows where to pick and return data.

# for gryfindor in sorted(gryfindors, key=lambda s: s["name"]):      
#     print(gryfindor["name"])

# #or

# students = [
#     {"name": "harry", "house": "gryfindor"},
#     {"name": "hermoine", "house": "slytherin"},
# ]

# gryfindors = filter(lambda s: s["house"] == "gryfindor", students)   # TODO: we don't have use a separate function and call it. we can directly give the return value in here as well.

# for gryfindor in sorted(gryfindors, key=lambda s: s["name"]):
#     print(gryfindor["name"])

# #TODO:

# #dict comprehension

# students = ["Harry","Hermoine","Ron"]

# gryfindors = []

# for student in students:
#     gryfindors.append({"name": student, "house": "gryfindor"})
    
# print(gryfindors)

# #or                                                                      # same as above here we are using list comprehension.

# students = ["Harry","Hermoine","Ron"]

# gryfindors = [{"name": student, "house": "gryfindor"} for student in students]

# print(gryfindors)

# #or                                                                     # using dict comprehension we are append directly the name value into key and house value into value    

# students = ["Harry","Hermoine","Ron"]

# gryfindors = [{student: "gryfindor"} for student in students]

# print(gryfindors)


#TODO:

#enumerate function

# students = ["Harry","Hermoine","Ron"]

# for i in range(len(students)):
#     print(i+1, students[i])

# #or TODO: enumerate goes through each index and its values and return them without directly calling the index of the value.

# students = ["Harry","Hermoine","Ron"]

# for i, student in enumerate(students):   # we have to give range of len(students). enumerate will pick automatically on whole.
#     print(i+1, student)

#TODO:

#generators - generates the new value each time for a loop. rather than adding values into same results of same iteration.

def main():
    n = int(input("enter n: "))
    for s in sheep(n):
        print(s)


# def sheep(n):
#     flock = []
#     for i in range(n):
#         print("*"*i)
#     return flock

#or

def sheep(n):
    for i in range(n):                   # yield funtion gives the result of each iteration as indivdual result rather than combined.
        yield "*"*i                      # this method saves memory, iterator function.

if __name__ == "__main__":
    main()

