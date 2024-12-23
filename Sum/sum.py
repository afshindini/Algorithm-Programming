"""This is a solution for the sum problem"""

def sums() -> None:
    """Check if one value is sum of the ther two"""
    number = int(input())
    for _ in range(number):
        values = list(map(int, input().split(" ")))
        max_val = max(values)
        if sum(values) == 2*max_val:
            print("YES") 
        else:
            print("NO")

if __name__ == "__main__":
    sums()
