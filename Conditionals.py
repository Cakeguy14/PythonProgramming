TODO:
#if statements - a control flow statement that allows you to execute different blocks of code based on certain conditions.

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} is equal to {y}")

#or - stands for logical OR, which returns True if at least one of the conditions is True.
if x > y or x < y:
    print(f"{x} and {y} are not equal")
else:
    print(f"{x} and {y} are equal")

#modulus operator - represented by the % symbol, it returns the remainder of a division operation.

if x % 2 == 0:
    print(f"{x} is an even number")
else:
    print(f"{x} is an odd number")

def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print(f"{x} is an even number")
    else:
        print(f"{x} is an odd number")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

TODO:
#match, case statements - a control flow statement that allows you to execute different blocks of code based on the value of a variable.

name = input("Enter your name: ")

match name:
    case "Harry":
        print("Hello, Harry!")
    case "Ron":
        print("Hello, Ron!")
    case "Hermione":
        print("Hello, Hermione!")
    case _:
        print("Hello, stranger!")

#or

match name:
    case "Harry" | "Ron" | "Hermione":
        print(f"Hello, {name}!")
    case _:
        print("Hello, stranger!")




