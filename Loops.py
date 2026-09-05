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

