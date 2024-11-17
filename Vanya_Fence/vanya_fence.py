"""This is a solution for vanya and fence problem"""

def vanya_fence() -> int:
    """Returns minimum width of the road"""
    _, fence_height = map(int, input().split(" "))
    heights = list(map(int, input().split(" ")))
    return sum(1 if height <= fence_height else 2 for height in heights)



if __name__ == "__main__":
    print(vanya_fence())
