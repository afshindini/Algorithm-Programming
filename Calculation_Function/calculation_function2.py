"""This is a solution for calculation function problem"""
import math

def calculation_function() -> int:
    """Returns the value of the function"""
    number = int(input())
    return number//2 - number%2*number



if __name__ == "__main__":
    print(calculation_function())
