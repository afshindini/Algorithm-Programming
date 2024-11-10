"""This is a solution for stone on the table problem"""

def stone_table() -> int:
    """Find number of stones be taken out"""
    numbers = int(input("Enter the numbers of stones: "))
    stones = input("Enter the RGB stones: ")
    return sum(1 for id in range(numbers-1) if stones[id] == stones[id+1])



if __name__ == "__main__":
    print(stone_table())
    