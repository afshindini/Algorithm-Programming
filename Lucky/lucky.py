"""This is a solution for the Lucky problem"""

def lucky() -> None:
    """Print if the number on the ticket is lucky or not"""
    test_cases = int(input())
    for _ in range(test_cases):
        values = list(map(int, input()))
        if sum(values[:3]) == sum(values[3:]):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    lucky()
