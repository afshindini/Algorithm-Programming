"""This is a solution for the Vasya Hipster problem"""

from typing import Tuple
def vasya_hipster() -> Tuple[int, int]:
    """Return the number of different socks and same socks"""
    red, blue = map(int, input().split(" "))
    different_socks = min([red, blue])
    return different_socks, (max([red, blue]) - different_socks)//2

if __name__ == "__main__":
    print(*vasya_hipster())
