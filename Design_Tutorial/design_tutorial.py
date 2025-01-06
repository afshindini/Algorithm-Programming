"""This is a solution for the Desinbg Tutorial problem"""
from typing import List, Optional

def is_composite(number: int) -> bool:
    """Check if a number is composite or not"""
    for elem in range(2, int(number**0.5)+1):
        if number%elem == 0:
            return True
    return False

def design_tutorial() -> Optional[List[int]]:
    """Express each number as two composite number"""
    number = int(input())
    for num1 in range(4, number//2+1):
        if is_composite(num1) and is_composite(number-num1):
            return [num1, number-num1]
    return None


if __name__ == "__main__":
    result = design_tutorial()
    if result is not None:
        print(*result)
