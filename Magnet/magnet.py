"""This is a solution for magnet problem"""

def magnet() -> int:
    """Returns the number of groups of magnets"""
    number_magnets = int(input())

    for idx in range(number_magnets):
        if idx == 0:
            magnets = int(input())
            result = 1
            continue
        temp = int(input())
        if magnets != temp:
            result +=1
            magnets = temp
    return result



if __name__ == "__main__":
    print(magnet())
