"""This is a solution for the Short Sort problem"""

def short_sort() -> None:
    """Check if the sort algorithms can be applied"""
    test_cases = int(input())
    for _ in range(test_cases):
        cards = list(input())
        if cards[0] == 'a' or cards[1] == 'b' or cards[2] =='c':
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    short_sort()
