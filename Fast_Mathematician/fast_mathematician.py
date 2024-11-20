"""This is a solution for ultra fast mathematician problem"""

def fast_xor() -> str:
    """Returns the volume fraction in orange juice cocktail"""
    val1 = input()
    val2 = input()
    return f"{int(val1, 2)^int(val2, 2):b}".zfill(len(val1))



if __name__ == "__main__":
    print(fast_xor())
