"""This is a solution for sum of round numbers problem"""

def sum_round() -> None:
    """Print the list of round numbers that sums the original one"""
    amount = int(input())
    for _ in range(amount):
        number_str = input()
        values = [int(number_str[idx])*(10**(len(number_str)-1-idx))
                  for idx in range(len(number_str)) if number_str[idx] != '0']
        print(len(values))
        print(*values)


if __name__ == "__main__":
    sum_round()
