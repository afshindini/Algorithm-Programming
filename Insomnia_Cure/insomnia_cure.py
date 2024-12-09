"""This is a solution for insomnia cure problem"""

def insomnia_cure() -> int:
    """Return the number of damaged dragons"""
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    return sum(1 for id in range(1, d+1) if id%k==0 or id%l==0 or id%m==0 or id%n==0)

if __name__ == "__main__":
    print(insomnia_cure())
