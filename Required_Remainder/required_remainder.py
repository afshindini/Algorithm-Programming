"""This is a solution for the Required Remainder problem"""

def required_remainder() -> None:
    """Print the largets number that is less than n and is divisible by x"""
    test_cases = int(input())
    for _ in range(test_cases):
        x, y, n = map(int, input().split(" "))
        print((n - y) // x * x + y)


if __name__ == "__main__":
    required_remainder()
