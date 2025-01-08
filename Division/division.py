"""This is a solution for the Divisiom problem"""

def division() -> None:
    """Print if the number on the ticket is lucky or not"""
    test_cases = int(input())
    for _ in range(test_cases):
        rate = int(input())
        if rate <= 1399:
            print("Division 4")
        elif 1400<=rate <= 1599:
            print("Division 3")
        elif 1600<=rate <= 1899:
            print("Division 2")
        else:
            print("Division 1")

if __name__ == "__main__":
    division()
