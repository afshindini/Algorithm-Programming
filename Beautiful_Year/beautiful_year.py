"""This is a solution for beautiful year problem"""

def beautiful_year() -> int:
    """Returns a year with distinct digits larger than the input year"""
    year = int(input())
    year +=1
    while len(set(str(year))) != len(str(year)):
        year += 1
    return year



if __name__ == "__main__":
    print(beautiful_year())
