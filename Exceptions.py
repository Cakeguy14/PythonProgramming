TODO:
#syntax error - occurs when the Python parser detects an incorrect statement

#value error - occurs when a function receives an argument of the right type but inappropriate value

TODO:
#try and except - used to handle exceptions in Python. The code inside the try block is executed, and if an exception occurs, the code inside the except block is executed.

try:
    n = int(input("Enter a number: "))
    print(f"You entered: {n}")
except ValueError:
    print("That's not a valid number. Please enter an integer.")

#name error - occurs when a local or global name is not found
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number. Please enter an integer.")

print(f"You entered: {n}")


#correct method to handle exceptions using try and except blocks. Print within the else block will only execute if no exception occurs in the try block.
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number. Please enter an integer.")
else:
    print(f"You entered: {n}")

#handling exceptions using wwhile loop to keep prompting the user until a valid input is received.

while True:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("That's not a valid number. Please enter an integer.")
    else:
        break

print("f""You entered: {n}")

#using functions

def main():
    x = get_number()
    print(f"You entered: {x}")

def get_number():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("That's not a valid number. Please enter an integer.")
        else:
            return x

main()

TODO:
#pass - The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

def main():
    x = get_number()
    print(f"You entered: {x}")

def get_number():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass  # Do nothing and continue the loop

main()

#parameter in function to handle exceptions
def main():
    x = get_number("Enter a number: ")
    print(f"You entered: {x}")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt)) #parameter is a placeholder for the input message that will be passed to the function when it is called.
        except ValueError:
            pass

main()

TODO:
#finally - The finally block is used to execute code regardless of whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.
def main():
    x = get_number("Enter a number: ")
    print(f"You entered: {x}")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        finally:
            print("Wrong input. Please try again.")

main()

TODO:
#raise - The raise statement is used to raise an exception. You can use it to trigger an exception when a certain condition is met.

def main():
    x = get_number("Enter a number: ")
    print(f"You entered: {x}")

def get_number(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x < 0:
                raise ValueError("Negative numbers are not allowed.")
            return x
        except ValueError as e:
            print(e)

main()