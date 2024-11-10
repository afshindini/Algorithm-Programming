"""This is a solution word problem"""

def word() -> str:
    """Return the appropriate upper/lower case form"""
    string = input("Enter string: ")
    if sum(map(str.islower, string)) < sum(map(str.isupper, string)):
        return string.upper()

    return string.lower()
        


if __name__ == "__main__":
    print(word())
    