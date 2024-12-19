"""This is a solution for candies and sisters problem"""

def candies_sisters() -> None:
    """Print the number of possible solutions fro dividing the candies"""
    cases = int(input())
    for _ in range(cases):
        candies = int(input())
        if candies - (candies//2+1) > 0 :
            print(candies - (candies//2+1))
        else:
            print(0)

if __name__ == "__main__":
    candies_sisters()
