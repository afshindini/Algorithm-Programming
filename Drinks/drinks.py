"""This is a solution for drinks problem"""

def drink() -> float:
    """Returns the volume fraction in orange juice cocktail"""
    number = int(input())
    return sum(map(int, input().split(" ")))/number



if __name__ == "__main__":
    print(drink())
