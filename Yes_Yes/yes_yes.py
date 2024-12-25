"""This is a solution for the Yes and Yes problem"""

def yes_yes() -> None:
    """Print if the string is YES or not"""
    number = int(input())
    for _ in range(number):
        input_string = input().lower()
        if input_string == 'yes':
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    yes_yes()
