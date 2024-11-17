"""This is a solution for queue at school problem"""

def queue_school() -> str:
    """Returns the rearranged queue"""
    _, times = map(int, input().split(" "))
    queue = list(input())
    for _ in range(times):
        boy_indices = [idx for idx,char in enumerate(queue) if char == 'B']
        for idx in boy_indices:
            if idx < len(queue)-1 and queue[idx+1] == 'G':
                queue[idx] = 'G'
                queue[idx+1] = 'B'
    return ''.join(queue)



if __name__ == "__main__":
    print(queue_school())
