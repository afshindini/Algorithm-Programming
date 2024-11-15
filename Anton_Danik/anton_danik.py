"""This is aolustion for anton and danik problem"""

def anton_danik() -> str:
    """return the name of the person who won more chess games"""
    _ = int(input())
    winners = input()
    anton = winners.count('A')
    danik = winners.count('D')
    if anton > danik:
        result = 'Anton'
    elif anton < danik:
        result = "Danik"
    else:
        result = "Friendship"
    return result



if __name__ == "__main__":
    print(anton_danik())
