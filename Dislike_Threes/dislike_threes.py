"""This is a solution for the Dislike of Threes problem"""

def dislike_threes() -> None:
    """Print the series of number not divisable by 3 neither has right most digit as 3"""
    test_cases = int(input())
    for _ in range(test_cases):
        number = int(input())
        count = 0
        result = 0
        while count < number:
            result +=1
            if result%3 !=0 and result%10 !=3:
                count +=1
        print(result)


if __name__ == "__main__":
    dislike_threes()
