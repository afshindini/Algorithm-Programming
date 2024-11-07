"""This is a solution for domino piling problem"""

def domino_piling() -> int:
    """Return the number dominos that can fit the pile"""
    m_value, n_value = map(int, input("Enter the size of the pile as MxN: ").split(" "))
    return m_value*n_value//2


if __name__ == "__main__":
    print(domino_piling())