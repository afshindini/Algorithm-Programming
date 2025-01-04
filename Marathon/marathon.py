"""This is a solution for the Marathon problem"""

def marathon() -> None:
    """Return thenumber of participants"""
    test_cases = int(input())
    for _ in range(test_cases):
        values = list(map(int, input().split(" ")))
        print(sum(1 for elem in range(1, len(values)) if values[elem] > values[0]))

if __name__ == "__main__":
    marathon()
