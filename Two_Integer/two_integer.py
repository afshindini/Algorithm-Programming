"""This is a solution for the Two Integer problem"""

def two_integer() -> None:
    """Print the minimum number of required addition/substraction"""
    test_cases = int(input())
    for _ in range(test_cases):
        a, b = map(int, input().split(" "))
        diff = abs(a-b)
        if diff%10 == 0:
            print(diff//10)
        else:
            print(diff//10+1)



if __name__ == "__main__":
    two_integer()
