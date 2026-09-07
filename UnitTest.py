#TODO:

#unit testing - Testing the given python file and functions within the file, when called in another file.

def main():
    print(square(3))

def square(n): #n inside the bracket of function is called the local variable/parameter/placeholder. This helps the function to take the returning value and send it elsewhere.
    return  n * n

if __name__ == "__main__":
    main()

# TODO:

def main():
    n = input("Enter your name bro: ")
    print(hello(n))


def hello(to="All"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()