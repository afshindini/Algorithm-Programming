"""This is a solution for amusing joke problem"""

def amusing_joke() -> str:
    """Check if the mixed names contains all the letters of individuals"""
    first = list(input())
    second = list(input())
    mixed = list(input())
    piles = first + second
    piles.sort()
    mixed.sort()
    if piles == mixed:
        return "YES"
    return "NO"

if __name__ == "__main__":
    print(amusing_joke())
