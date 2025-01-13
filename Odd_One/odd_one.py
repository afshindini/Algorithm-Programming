"""This is a solution for the Odd One Out problem"""

def odd_one() -> None:
    """Find the odd number between three numbers"""
    test_cases = int(input())
    for _ in range(test_cases):
        values = list(map(int, input().split(" ")))
        values.sort()
        if values[0] == values[1]:
            print(values[2])
        else:
            print(values[0])

if __name__ == "__main__":
    odd_one()
