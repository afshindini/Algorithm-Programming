"""Solution for nearly lucky number problem"""

def lucky_number() -> str:
    """Check if the number of 4,7 digits in a number is 4 or 7 or not"""
    number = input("")
    length = sum(1 if (digit in ['4', '7']) else 0 for digit in number)
    return "YES" if length in [4,7] else "NO"


if __name__ == "__main__":
    print(lucky_number())
