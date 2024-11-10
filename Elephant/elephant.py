"""This is a solution elephant problem"""

def elephant() -> int:
    """Find the minimum number of steps to reach the destination"""
    distance = int(input("Enter distance: "))
    return int(distance//5) if distance%5==0 else int(distance//5)+1


if __name__ == "__main__":
    print(elephant())
    