"""This is a solution for queue at school problem"""

def queue_school() -> str:
    """Returns the rearranged queue"""
    _, times = map(int, input().split(" "))
    queue = input()
    while times:
        queue = queue.replace('BG', 'GB')
        t -= 1
    return queue



if __name__ == "__main__":
    print(queue_school())
