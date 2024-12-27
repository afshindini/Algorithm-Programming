"""This is a solution for the sereja and dima problem"""

from typing import Tuple
def sereja_dima() -> Tuple[int,int]:
    """Return sum of cards of each players"""
    amount = int(input())
    numbers = list(map(int, input().split(" ")))
    turn, first_player, second_player = 0, 0, 0
    left_idx, right_idx = 0, amount-1
    while amount >0:
        if numbers[left_idx] > numbers[right_idx]:
            pickup_val = numbers[left_idx]
            left_idx +=1
        else:
            pickup_val = numbers[right_idx]
            right_idx -=1
        if turn%2==0:
            first_player += pickup_val
        else:
            second_player += pickup_val
        turn += 1
        amount -=1
    return first_player, second_player


if __name__ == "__main__":
    print(*sereja_dima())
