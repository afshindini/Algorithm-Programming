"""This is a solution for anton and letters problem"""

def anton_letters() -> int:
    """Return the number of damaged dragons"""
    return len(set(filter(None, input()[1:-1].replace(" ", "").split(","))))


if __name__ == "__main__":
    print(anton_letters())
