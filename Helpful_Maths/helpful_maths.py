"""This is a solution for helpful maths problem"""


def helpful_maths() -> str:
    """Return the math equation in non increasing order"""
    eq = input("Enter the sum equation only containing 1/2/3/+: ").split("+")
    eq.sort()
    return "+".join(eq)



if __name__ == "__main__":
    print(helpful_maths())
    