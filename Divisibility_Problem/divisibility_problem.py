"""This is a solution for divisibility problem"""

def divisibility() -> None:
    """Print the value that needs to be added to be visible"""
    number = int(input())
    for _ in range(number):
        val1, val2 = map(int, input().split(" "))
        print(val2 - val1%val2 if val1%val2 !=0 else 0)


if __name__ == "__main__":
    divisibility()
