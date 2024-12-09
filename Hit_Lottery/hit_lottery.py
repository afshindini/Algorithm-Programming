"""This is a solution for hit thr lottery problem"""

def hit_lottery() -> int:
    """Return the number of bills"""
    amount = int(input())
    count = 0
    for bill in [100, 20, 10, 5, 1]:
        count += amount//bill
        if amount%bill == 0:
            break
        amount = amount%bill    
    return count

if __name__ == "__main__":
    print(hit_lottery())
