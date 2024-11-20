"""This is a solution for george accommodation problem"""

def george_accommodation() -> int:
    """Returns qavailable room for george and alex"""
    number_rooms = int(input())
    result = 0
    for _ in range(number_rooms):
        filled, capcity = map(int, input().split(" "))
        if capcity - filled >=2:
            result += 1
    return result



if __name__ == "__main__":
    print(george_accommodation())
