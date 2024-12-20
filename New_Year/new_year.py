"""This is a solution for new year problem"""

def new_year() -> int:
    """Return the minimum distance that they should travel"""
    values = list(map(int, input().split(" ")))
    values.sort()
    return values[1] - values[0] + values[2] - values[1]


if __name__ == "__main__":
    print(new_year())
