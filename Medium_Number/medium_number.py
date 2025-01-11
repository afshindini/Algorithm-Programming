"""This is a solution for the Medium Number problem"""

def medium_number() -> None:
    """Print the medium number of three numbers"""
    test_cases = int(input())
    for _ in range(test_cases):
        values = list(map(int, input().split(" ")))
        values.sort()
        print(values[1])


if __name__ == "__main__":
    medium_number()
