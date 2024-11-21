"""This is a solution for horse shoe problem"""

def horse_shoe() -> int:
    """return minimum number of horse shoe that is needed"""
    colors = set(map(int, input().split(" ")))
    return 4 - len(colors)



if __name__ == "__main__":
    print(horse_shoe())
