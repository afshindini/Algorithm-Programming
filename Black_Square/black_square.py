"""This is a solution for the Black Square problem"""

def black_square() -> None:
    """Print the medium number of three numbers"""
    a1, a2, a3, a4 = map(int, input().split(" "))
    s = input()
    calories = 0
    for c in s:
        if c == "1":
            calories += a1
        elif c == "2":
            calories += a2
        elif c == "3":
            calories += a3
        elif c == "4":
            calories += a4
    print(calories)


if __name__ == "__main__":
    black_square()
