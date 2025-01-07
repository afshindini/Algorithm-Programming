"""This is a solution for the Choosing Team problem"""

def choosing_team() -> int:
    """Find the number possible teams"""
    _, k = map(int, input().split(" "))
    values = list(map(int, input().split(" ")))
    candidates = sum(1 for elem in values if elem <=5-k)
    return candidates//3


if __name__ == "__main__":
    print(choosing_team())
