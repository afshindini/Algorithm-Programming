"""This is a solution for the Balanced Array problem"""

def balanced_array() -> None:
    """Check if the algorithm is valid for integer n or not"""
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        if n % 4 != 0:
            print("NO")
        else:
            print("YES")
            even_numbers = list(range(2, n + 1, 2))
            odd_numbers = list(range(1, n, 2))
            odd_numbers[-1] += n // 2
            array = even_numbers + odd_numbers
            print(" ".join(map(str, array)))



if __name__ == "__main__":
    balanced_array()
