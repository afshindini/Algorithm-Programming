"""This is a solution for the Mishka and Game problem"""

def mishka_game() -> str:
    """Return the name of the winner"""
    game_runs = int(input())
    mishak_wins , chirs_wins = 0, 0
    for _ in range(game_runs):
        m, c = map(int, input().split(" "))
        if m>c:
            mishak_wins +=1
        elif m<c:
            chirs_wins +=1
        else:
            mishak_wins +=1
            chirs_wins +=1
    if mishak_wins > chirs_wins:
        return "Mishka"
    elif mishak_wins < chirs_wins:
        return "Chris"       
    return "Friendship is magic!^^"


if __name__ == "__main__":
    print(mishka_game())
