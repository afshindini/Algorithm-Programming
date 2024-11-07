"""Solution to next round problem"""

def next_round() -> int:
    """Return the number of contestants for next round"""
    _, place = map(int, input("Enter the number of contestants and kth-place seperated by space: ").split(" "))
    scores = list(map(int,input("Enter n scores seperated by space: ").split(" ")))
    return sum(1 if score >= scores[place-1] and score >0 else 0 for score in scores )


if __name__ == "__main__":
    print(next_round())