"""This is a solution for the Plus or Minus problem"""

def plus_minus() -> None:
    """Print the the operation of three numbers"""
    test_cases = int(input())
    for _ in range(test_cases):
        values = list(map(int, input().split(" ")))
        if values[0] + values[1] == values[2]:
            print('+')
        else:
            print('-')


if __name__ == "__main__":
    plus_minus()
