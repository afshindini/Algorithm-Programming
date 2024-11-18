"""This is a solution for in search of problem"""

def search_easy() -> str:
    """Returns EASY or HARD depending on the number of votes"""
    _ = int(input())
    votes = input().split(" ")
    return "HARD" if '1' in votes else "EASY"




if __name__ == "__main__":
    print(search_easy())
