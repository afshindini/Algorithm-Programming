"""This is a solution for games problem"""

def games() -> int:
    """Return the number of games with host uniform instead of home uniform"""
    numbers = int(input())
    homes, guests = [], []
    for _ in range(numbers):
        home, guest = map(int, input().split(" "))
        homes.append(home)
        guests.append(guest)
    count = 0
    for elem in set(homes):
        count += homes.count(elem) * guests.count(elem)

    return count


if __name__ == "__main__":
    print(games())
