"""This is a solution for the restoring three numbers problem"""

from typing import List

def restore_numbers() -> List[int]:
    """Return the three numbers"""
    values = list(map(int, input().split(" ")))
    max_val = max(values)
    numbers = [max_val - val for val in values if val != max_val]
    return numbers


if __name__ == "__main__":
    print(*restore_numbers())
