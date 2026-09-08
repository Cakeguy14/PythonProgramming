# # #TODO:

# # #input - output - functionality to open a new file from this file and append/write from this file.

name = input("Enter the name: ")

f = open("inputoutput.txt", "a")
f.write(name + "\n")
f.close()

# # # #or the below file=f funtion automatically considers \n as per the print default state - print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

f = open("inputoutput.txt", "a")
print(name, file=f)
f.close()

# # # #or - we can also shrink to below as well. with - with statement. Only difference is that the with statement automatically closes the file.

with open("inputoutput.txt", "a") as f:
    print(name, file=f)

# # #TODO:
# # #using sorted function to sort the values from the file that is read.
names = []

with open("inputoutput.txt") as f:
    lines = f.readlines()
    print(lines)

# # #or - instead of using readlines,use as below. rstrip() removes the \n hidden in each line txt file.

with open("inputoutput.txt") as f:
    for line in sorted(f):
        name = line.rstrip()
        names.append(name)
        print("Hello", name)

# print(names)

# #or - case sensitivity use key=str.lower

with open("inputoutput.txt") as f:
    for line in sorted(f, key=str.lower, reverse=True):
        name = line.rstrip()
        names.append(name)
        print("Hello", name)

print(names)

#TODO:

#split functionality allows you to separate any given string using split funtion. ex: CSV.

with open("inputoutput.txt") as f:
    for line in f:
        row = line.rstrip().split(",")
        print(f"{row[0]} is from house {row[1]}")

# #or

with open("inputoutput.txt") as f:
    for line in f:
        name, house = line.rstrip().split(",")
        print(f"{name} is from house {house}")

#TODO:

#To make the input variables collect as dictory and then send that dictionary to list to make a list of dictionaries.

students = []

with open("inputoutput.txt") as f:
    for line in f:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in house {student['house']}")

#or

with open("inputoutput.txt") as f:
    for line in f:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):                #python allows you to give one functions as argument to another functions
    return student["name"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in house {student['house']}")

print(students)

with open("inputoutput.txt") as f:
    for line in f:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):     #instead giving an independent function, we can use lambda function just incase we want to call/use that function only once/place and elsewhere 
    print(f"{student['name']} is in house {student['house']}")

#TODO:

#csv library

import csv

students = []

with open("inputoutput.txt") as f:
    reader = csv.reader(f)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):     #instead giving an independent function, we can use lambda function just incase we want to call/use that function only once/place and elsewhere 
    print(f"{student['name']} is in house {student['home']}")
print(students)


#TODO:
#or - we can use dictreader to read as a dictionary instead of reading as list(reader)


with open("inputoutput.txt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})   #when a dictreader is used you can use normal local variable name instead of calling the keys explicitly. this allows you to swap columns positions.

for student in sorted(students, key=lambda student: student["name"]):     #instead giving an independent function, we can use lambda function just incase we want to call/use that function only once/place and elsewhere 
    print(f"{student['name']} is in house {student['home']}")
print(students)


#TODO:

#writing into the file as both list and dictionary

import csv

name = input("Enter the Name: ")
home = input("Enter the home: ")

# with open("inputoutput.txt", "a") as f:
#     writer = csv.writer(f)
#     writer.writerow([name, home])

# #or

with open("inputoutput.txt", "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name","home"])
    writer.writeheader()
    writer.writerow({"name": name, "home": home})
print(name,home)


#TODO:

#gif maker

import sys

from PIL import Image

images  = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save("sample.gif", save_all=True, append_images=[images[1]], duration=200, loop=0)
    





