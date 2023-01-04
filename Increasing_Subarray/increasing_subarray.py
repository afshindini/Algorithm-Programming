"""Count number of increasing subarray"""
from typing import Tuple


def count_long_subarray(arr: Tuple) -> int:
    """
    Input:  arr    | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    """
    count = 1
    longest_length = 1
    current_length = 1

    arr_len = len(arr)
    for i in range(1, arr_len):
        if arr[i - 1] < arr[i]:
            current_length += 1
        else:
            current_length = 1

        if current_length > longest_length:
            longest_length = current_length
            count = 1
        elif current_length == longest_length:
            count += 1
    return count


if __name__ == "__main__":
    inp = tuple(int(x.strip()) for x in input("Enter values: ").split(' '))
    print(inp)
    print("Number of long subarrays are: ", count_long_subarray(inp))
