"""This is a solution for the To My Critics problem"""

def my_critics() -> None:
    """Print the medium number of three numbers"""
    test_cases = int(input())
    for _ in range(test_cases):
        values = list(map(int, input().split(" ")))
        values.sort()
        if values[2]+values[1]>=10:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    my_critics()
