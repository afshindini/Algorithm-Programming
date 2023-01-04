"""Watermelon problem, first solution"""

def watermelon1(input_weight: int) -> str:
    """First solution to solve the Watermelon problem"""
    return 'YNEOS'[5%~input_weight%2::2]

def watermelon2(input_weight: int) -> str:
    """Second solution to solve the Watermelon problem"""
    return "YES" if input_weight%2 == 0 and input_weight > 2 else "NO"


if __name__ == "__main__":
    weight = int(input("Insert the weight: "))
    print("Results from Watermelon1: ", watermelon1(weight))
    print("Results from Watermelon2: ", watermelon2(weight))
