"""This is a solution soldiers and bananas problem"""

def soldiers_bananas() -> int:
    """Find the amount money the soldier has to borrow to buy bananas"""
    inputs = list(map(int,input("Enter price of each banana, initial asset, and number of bananas: ").split(" ")))
    bananas_price = int(inputs[0]*inputs[2]*(inputs[2]+1)/2)
    return bananas_price - inputs[1] if bananas_price > inputs[1] else 0


if __name__ == "__main__":
    print(soldiers_bananas())
    