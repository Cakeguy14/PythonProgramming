# TODO:
# #modules - A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Modules can define functions, classes, and variables, 
# #           and can also include runnable code.

# #random - The random module provides functions that support many operations. It includes functions for generating random numbers, selecting random items from a list, shuffling a list, and more.
# import random
# from random import randint, choice

# coin = choice(["Heads", "Tails"])
# num = randint(1, 100)
# dummy = ["apple", "banana", "cherry", "date"]
# random.shuffle(dummy)
# print(coin)
# print(num)
# for fruit in dummy:
#     print(fruit)

# TODO:
# #statistics - The statistics module provides functions for calculating mathematical statistics of numeric data. 
# #              It includes functions for calculating mean, median, mode, variance, standard deviation,
# #             and more.
# import statistics

# print("Mean:", statistics.mean([100,90]))

# TODO:
# #sys - The sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. 
# #       It allows you to manipulate Python runtime environment.

# import sys

# print("hi, your name is? ", sys.argv[1])

# #or

# if len(sys.argv) > 2:
#     print("Too many arguments!")
# elif len(sys.argv) < 2:
#     print("Too few arguments!")
# else:
#     print("Hello, ", sys.argv[1])

# #python Libraries.py "Senthur Kumaran"

# #sys.exit - The sys.exit() function is used to exit from Python.
# #   It can be used to terminate a program and optionally pass an exit status code. 
# #   If the status code is omitted or None, it defaults to zero (indicating successful termination). 
# #   A non-zero value indicates an error or abnormal termination.

# if len(sys.argv) > 2:
#     sys.exit("Too many arguments!")
# elif len(sys.argv) < 2:
#     sys.exit("Too few arguments!")

# print("Hello, ", sys.argv[1])

# #slice - The slice() function returns a slice object that can be used to slice a sequence (like a list, tuple, or string).

# if len(sys.argv) > 2:
#     sys.exit("Too many arguments!")
# for arg in sys.argv[1:]:
#     print("Hello, :", arg)

# #or

# if len(sys.argv) > 2:
#     sys.exit("Too many arguments!")
# for arg in sys.argv[1:-1]: # negative index -1 means the last element of the list, so [1:-1] means all elements from index 1 to the second last element.
#     print("Hello, :", arg)

# TODO:
# #packages - A package is a way of organizing related modules into a single directory hierarchy.

# #pip - pip is a package manager for Python that allows you to install and manage additional libraries and dependencies that are not included in the standard library.

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("Hello, " + sys.argv[1])

# TODO:
# #API - An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other.

# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit("Usage: python Libraries.py band_name")

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# #print(json.dumps(response.json(), indent=2))

# o = response.json()
# for result in o["results"]:
#     print(result["trackName"])


# TODO:
#own library - You can create your own library by creating a Python file with functions, classes, and variables that you want to reuse in other programs.

def main():
    greet("Senthur Kumaran")
    farewell("Senthur Kumaran")


def greet(name):
    print(f"Hello, {name}")

def farewell(name):
    print(f"Goodbye, {name}")

#main()


if __name__ == "__main__":
    main()