"""This is a solution for the remove smallest problem"""

def remove_smallest() -> None:
    """Print YES/NO whether the algorithm is applicable or not"""
    test_cases = int(input())
    for _ in range(test_cases):
        result = "YES"
        _ = int(input())
        numbers = list(map(int, input().split(" ")))
        numbers.sort()
        for idx in range(1,len(numbers)):
            if numbers[idx]-numbers[idx-1] >1:
                result = "NO"
                break
        if result == "NO":
            print(result)
        else:
            print("YES")




if __name__ == "__main__":
    remove_smallest()
