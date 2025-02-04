"""This is a solution for the Love Story problem"""

def love_story() -> None:
    """Print the numbers of different letters in the strings"""
    test_cases = int(input())
    for _ in range(test_cases):
        values = input()
        print(sum(1 for i, val in enumerate("codeforces") if values[i]!=val))


if __name__ == "__main__":
    love_story()
