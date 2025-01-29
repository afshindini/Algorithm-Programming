"""This is a solution for the Panorama Prediction problem"""

def panorama_prediction() -> None:
    """Print if the two numbers are prime values one after the other"""
    n, m = map(int, input().split())
    if is_prime(n) and is_prime(m):
        for i in range(n + 1, m):
            if is_prime(i):
                print("NO")
                return
        print("YES")
    else:
        print("NO")


def is_prime(number: int) -> bool:
    """Return if the number is prime"""
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    panorama_prediction()
