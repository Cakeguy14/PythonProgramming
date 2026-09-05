TODO:
#Loops - For and While loops

#while loop - repeats a block of code as long as a condition is true

i = 4

while i != 0:
    print("Hi")
    i = i - 1

#or

i = 1

while i <= 4:
    print("Hi")
    i += 1 - #same as i = i + 1

TODO:
#for loop - repeats a block of code for a specified number of times
#for loop is used when the number of iterations is known in advance

#list - a collection of items

for i in [0, 1, 2, 3]:
    print("Hi")

#or

for i in range(4):
    print("Hi")

#i - is not defined outside the loop, it is only defined within the loop
    #it can be used as a counter variable to keep track of the number of iterations
    #it can be either i or _ or any other variable name

#or

print("Hi\n" * 4, end="") - #prints "Hi" 4 times, each on a new line

TODO:
#while loop - repeats a block of code as long as a condition is true

while True:
    n = int(input("Enter a positive integer: "))
    if n > 0:
        break

for _ in range(n):
    print("Hi")

#using functions to avoid code repetition

def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("Meow")

main() - #calls the main function

#or

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter a positive integer: "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()

TODO:
#list - a collection of items

students = ["Hermoine", "Harry", "Ron"]

for student in students:
    print(student)

#len() - returns the number of items in a list

print(len(students)) - #prints 3

for student in range(len(students)): #range() - returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
    print(student + 1, students[student]) - #prints each student in the list

#dict - a collection of key-value pairs

students = {
    "Hermoine": "Granger",
    "Harry": "Potter",
    "Ron": "Weasley"
}

print(students["Hermoine"])  #unlike lists, dictionaries are unordered, so you cannot access items by index, but by key

for each in students:
    print(each, students[each])  #prints each key-value pair in the dictionary
    print(each, students[each], sep=", ")