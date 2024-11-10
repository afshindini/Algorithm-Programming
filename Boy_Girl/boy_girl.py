"""This is a solution for boys or girls problem"""


def boy_girl() -> str:
    """Check if the number of unique values in the username is odd or even"""
    username = set(input("Enter the username: "))
    return "CHAT WITH HER!" if len(username)%2==0 else "IGNORE HIM!"


if __name__ == "__main__":
    print(boy_girl())
    