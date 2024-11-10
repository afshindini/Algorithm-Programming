"""This is a solution wrong subtraction problem"""

def wrong_subtraction() -> int:
    """Return the appropriate upper/lower case form"""
    inputs = list(map(float,input("Enter number and number of substraction: ").split(" ")))
    for _ in range(int(inputs[1])):
        inputs[0] = inputs[0] -1 if inputs[0]%10 != 0 else inputs[0]/10
    return int(inputs[0])

if __name__ == "__main__":
    print(wrong_subtraction())
    