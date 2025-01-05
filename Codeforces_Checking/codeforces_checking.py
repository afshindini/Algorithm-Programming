"""This is a solution for the Codeforces Checking problem"""

def checking() -> None:
    """Print the the operation of three numbers"""
    test_cases = int(input())
    for _ in range(test_cases):
        character = input()
        if character in 'codeforces':
            print("YES")
        else:
            print("NO")  


if __name__ == "__main__":
    checking()
