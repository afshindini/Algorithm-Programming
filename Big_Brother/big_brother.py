"""This is a solution for Bear and big brother problem"""
import math

def big_brother() -> int:
    """Return the math equation in non increasing order"""
    weights = list(map(int, input("Enter the weights separated by space: ").split(" ")))
    return int(math.log(weights[1]/weights[0])/math.log(1.5))+1



if __name__ == "__main__":
    print(big_brother())
    