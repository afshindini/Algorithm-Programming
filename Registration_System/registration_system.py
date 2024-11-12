"""This is a solution for registration system problem"""


def registration_system() -> None:
    """Print OK if a valid username unless print modified ones"""
    number_usernames = int(input("Enter number usernames: "))
    repeated_dict: dict[str, int] = {}
    results = []
    for idx in range(number_usernames):
        username = input(f"Enter {idx}th username: ")
        if username not in repeated_dict:
            results.append("OK")
            repeated_dict[username] = 0
        else:
            repeated_dict[username] = repeated_dict[username] + 1
            results.append(f"{username}{repeated_dict[username]}")

    for usr in results:
        print(usr)


if __name__ == "__main__":
    registration_system()
