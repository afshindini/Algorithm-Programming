"""This is a solution for the Creating Word problem"""

def creating_word() -> None:
    """Print two new words by swaping the first char of two words"""
    test_cases = int(input())
    for _ in range(test_cases):
        a, b = map(str, input().split(" "))
        print(b[0] + a[1:], a[0] + b[1:])

if __name__ == "__main__":
    creating_word()
