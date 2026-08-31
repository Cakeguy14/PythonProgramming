TODO: variables
#LHS = RHS -> RHS is the assignment value, LHS is the variable being assigned to.

#Arguments - values passed to a function when it is called.
#Parameters - variables that are defined in the function definition and receive the values of the arguments when the function is called.

TODO:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> prints the objects to the console or specified file with optional separators and end characters.

#positional parameters - parameters that are defined in a function and must be provided in the correct order when the function is called.
#named parameters - parameters that are defined in a function and can be provided in any order when the function is called, using the parameter name.

#objects - the values or variables to be printed.
#\n - newline character, used to create a new line in the output.
#sep - separator character, used to separate multiple objects in the output.
#file - specifies the file to which the output should be written, default is sys.stdout (console).
#flush - if True, the output is flushed (written) immediately to the file or console.

example:
word = input("Enter a word: ")
print("You entered:", word, sep=" ", end="\n") -> You entered: <user_input>
print(word)

TODO: 
#end="" or end="\n" - controls what is printed at the end of the output. 
#end="" means no newline character is printed, while end="\n" means a newline character is printed.

#escaping characters - special characters that are used to represent certain characters in a string, such as \n for newline, \t for tab, and \\ for backslash.

print("Hello, \"world\"!") -> Hello, "world"!

TODO:
#formatting strings - using special characters and placeholders to create formatted output.

print(f"You entered: {word}")

#Functions - blocks of code that perform a specific task and can be called multiple times with different arguments.

TODO:
#strip - removes leading and trailing whitespace from a string.

word = input("Enter a word: ").strip()

#or

word = word.strip()

#capitalize - converts the first character of a string to uppercase and the rest to lowercase.

word = word.capitalize()

#title - converts the first character of each word in a string to uppercase and the rest to lowercase.

word = word.title() 

word = word.strip().title()

#split - splits a string into a list of substrings based on a specified delimiter (default is whitespace).

word_list = word.split()

# first, second = word_list[0], word_list[1] -> assigns the first and second elements of the list to the variables first and second.

# print(first, second) -> prints the first and second elements.

first, last = word.split() -> splits the string into two parts and assigns them to the variables first and last.

print(first, last) -> prints the first and last names.

TODO:
#Data types - the classification of values in programming, such as strings, integers, floats, and booleans.

#str - a built-in Python class that represents a string of characters.
#int - a built-in Python class that represents an integer value.
#float - a built-in Python class that represents a floating-point value.
#operators - symbols that perform operations on values, such as + for addition, - for subtraction, * for multiplication, and / for division.

TODO:
#>>> - the Python interactive shell prompt, indicating that the following line is a command to be executed in the shell.


TODO:
#input() - a built-in Python function that reads a line of input from the user and returns it as a string.

x = input("Enter a number: ")
y = input("Enter a number: ")
c = int(x) + int(y)
print("The sum of", x, "and", y, "is", c)

#or

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(f"The sum of {x} and {y} is {x + y}")

#or

print("The sum of {} and {} is {}".format(x, y, x + y))

TODO:
#round - a built-in Python function that rounds a floating-point number to a specified number of decimal places.

Z = round(x/y, 2) 
print(f"{z:,}") - #prints the value of z with commas as thousands separators.
print(f"{z:.2f}") - #prints the value of z with two decimal places.

TODO:
#Functions -def - a keyword used to define a function in Python.

def hello(to="world"):
    print("hello,", to)

hello() -> #hello, world
name = input("Enter your name: ")
hello(name)

#function positional parameters - parameters that are defined in a function and must be provided in the correct order when the function is called.

def main():
    name = input("Enter your name: ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main() -> #hello, <user_input> - without the main() function, the hello() function would not be called and the program would not run. 
                                #why? Because the function is defined but never executed without being called from another function or directly in the script.

TODO:
#Return functions - functions that return a value to the caller using the return statement.

def main():
    x = int(input("Enter a number: "))
    print(f"The square of {x} is {square(x)}")

def square(n):
    return n ** 2

#or

def square(n):
    return pow(n, 2) -> #returns the value of n raised to the power of 2.

main()