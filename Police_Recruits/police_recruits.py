"""This is a solution for police recruiters problem"""

def police_recruiters() -> int:
    """Return the number of untreated crimes"""
    _ = int(input())
    values = list(map(int, input().split(" ")))
    sums, count = 0, 0
    for val in values:
        sums += val
        if sums < 0:
            sums = 0
            count +=1
    return count


if __name__ == "__main__":
    print(police_recruiters())
