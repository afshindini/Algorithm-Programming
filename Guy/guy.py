"""This is a solution for the guy problem"""

def guy() -> str:
    """Check if two players can pass the game"""
    number = int(input())
    player1 = list(map(int, input().split(" ")))
    player2 = list(map(int, input().split(" ")))
    if 0 in player1:
        player1.remove(0)
    if 0 in player2:
        player2.remove(0)
    
    return "I become the guy." if len(set(player1 + player2)) == number else "Oh, my keyboard!"


if __name__ == "__main__":
    print(guy())
