"""This is a solution for presents problem"""

def present() -> None:
    """Returns the number presents"""
    number=int(input())
    present_list = input().split(" ")
    print(*[present_list.index(str(i+1))+1 for i in range(number)])



if __name__ == "__main__":
    present()
