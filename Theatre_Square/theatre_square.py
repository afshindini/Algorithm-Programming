"""This is solution to theatre square problem"""

import math

def theatre_square() -> int:
    """Return the list number of tiles to pave the square"""
    n_val, m_val, a_val = map(int, input("").split(" "))
    height = 1 if n_val <= a_val else math.ceil(n_val/a_val)
    width = 1 if m_val <= a_val else math.ceil(m_val/a_val)
    return height * width

if __name__ == "__main__":
    print(theatre_square())
