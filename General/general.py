"""This is a solution for arrival of general problem"""

def general() -> int:
    """Return the number of moves for sorting"""
    count = int(input())
    numbers = list(map(int, input().split(" ")))
    max_index = numbers.index(max(numbers))
    min_index = count - 1 - numbers[::-1].index(min(numbers))
    temp = 1 if max_index - min_index > 0 else 0
    return count - 1 - min_index + max_index - temp



if __name__ == "__main__":
    print(general())
