"""This is a solution for the Holiday Equality problem"""

def holiday_equality() -> int:
    """Print the minimum number that should be added to equal others"""
    citizens = int(input())
    numbers = list(map(int, input().split(" ")))
    return citizens*max(numbers) - sum(numbers)


if __name__ == "__main__":
    print(holiday_equality())
