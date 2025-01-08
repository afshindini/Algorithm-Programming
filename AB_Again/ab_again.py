"""This is a solution for the A+B Again problem"""

def ab_again() -> None:
    """Print Sum of digits in a number"""
    test_cases = int(input())
    for _ in range(test_cases):
        number = input()
        print(int(number[0])+int(number[1]))


if __name__ == "__main__":
    ab_again()
