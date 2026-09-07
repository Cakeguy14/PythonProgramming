# TODO:

#unit testing - file 2
import pytest
from UnitTest import square

def main():
    test_square()

def test_square():
    try:
        assert square(3) == 9
    except AssertionError:
        print("The square value is incorrect")
    try:
        assert square(4) == 16
    except AssertionError:
        print("The square value is incorrect, Sir!")

#or

# def test_squares():
#     assert square(3) == 9, "This is correct"
#     asser square(4) == 16, "this is correct"

main()  

# TODO:

from UnitTest import hello

def test_hello():
    assert hello() == "Hello, All"
    assert hello("Senthur") == "Hello, Senthur"

