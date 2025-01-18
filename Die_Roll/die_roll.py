"""This is a solution for the Die Roll problem"""
from fractions import Fraction
from typing import Any

def die_roll() -> Any:
    """Return the probability of a dice value greater than the inputs"""
    x, y = map(int, input().split(" "))
    return Fraction(7-max(x, y), 6) if 1 < max(x, y) < 7 else '1/1' if  max(x,y) == 1 else '0/1'


if __name__ == "__main__":
    print(die_roll())
