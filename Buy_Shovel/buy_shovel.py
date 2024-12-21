"""This is a solution for the buy a shovel problem"""

def buy_shovel() -> int:
    """Return the minimum number of shovels"""
    k, r = map(int, input().split(" "))
    for number in range(1,10):
        if (number*k-r)%10 == 0 or (number*k)%10 == 0:
            return number
    return 10

if __name__ == "__main__":
    print(buy_shovel())
