"""This is a solution for the Stair Peak problem"""

def stair_peak() -> None:
    """Print the the types of numbers whether they are stairs, peaks or neither"""
    test_cases = int(input())
    for _ in range(test_cases):
        a, b, c = map(int, input().split(" "))
        if a < b < c:
            print("STAIR")
        elif a < b > c:
            print("PEAK")
        else:
            print("NONE")


if __name__ == "__main__":
    stair_peak()
