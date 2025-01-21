"""This is a solution for the Spy Detected problem"""

def spy_detected() -> None:
    """Print the index of unsimilar number in an array"""
    test_cases = int(input())
    for _ in range(test_cases):
        array_len = int(input())
        values = list(map(int, input().split(" ")))
        unique_values= list(set(values))
        if unique_values[0]*(array_len-1) + unique_values[1] == sum(values):
            print(values.index(unique_values[1])+1)
        else:
            print(values.index(unique_values[0])+1)


if __name__ == "__main__":
    spy_detected()
