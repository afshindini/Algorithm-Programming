"""This is a solution for the Minimize problem"""

def minimize() -> None:
    """Print the minimum value"""
    test_cases = int(input())
    for _ in range(test_cases):
        a, b = map(int, input().split(" "))
        print(b-a)


if __name__ == "__main__":
    minimize()
