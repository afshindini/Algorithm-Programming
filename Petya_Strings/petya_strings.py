"""This is a solution for petya strings"""


def petya_strings() -> int:
    """Return the number of moves to make matrix beautiful"""
    string1 = input("Enter the first strings of letters: ").lower()
    string2 = input("Enter the second strings of letters: ").lower()
    return 0 if string1 == string2 else 1 if string1>string2 else -1


if __name__ == "__main__":
    print(petya_strings())
    