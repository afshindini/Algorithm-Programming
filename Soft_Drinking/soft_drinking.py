"""This is a solution for the soft drinking problem"""

def soft_drinking() -> int:
    """Return the minimum number of toasts"""
    n, k, l, c, d, p, nl, np = map(int, input().split(" "))

    return min([(k*l)//nl, c*d, p//np])//n


if __name__ == "__main__":
    print(soft_drinking())
