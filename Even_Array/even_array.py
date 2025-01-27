"""This is a solution for the Even Array problem"""

def even_array() -> None:
    """Print the the number of move to make the array even"""
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        values = list(map(int, input().split(" ")))
        even_mismatch = 0
        odd_mismatch = 0
        for i in range(n):
            if values[i] % 2 != i % 2:
                if i % 2 == 0:
                    even_mismatch += 1
                else:
                    odd_mismatch += 1
        if even_mismatch == odd_mismatch:
            print(even_mismatch)
        else:
            print(-1)

if __name__ == "__main__":
    even_array()
