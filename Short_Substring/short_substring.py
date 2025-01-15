"""This is a solution for the Short Substring problem"""

def short_substring() -> None:
    """Print the original substring from the input string"""
    test_cases = int(input())
    for _ in range(test_cases):
        values = list(input())
        results = []
        results.append(values[0])
        for i in range(1, len(values)-1, 2):
            results.append(values[i])
        results.append(values[-1])
        print("".join(results))


if __name__ == "__main__":
    short_substring()
