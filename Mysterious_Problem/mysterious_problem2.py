"""This is a solution for mysterious problem"""

from bisect import bisect_left

def mysterious_problem() -> None:
    """Print the order of envelop and its increasing indices"""
    env_number, card_width, card_height = map(int,input().split(" "))
    data = []
    for idx in range(env_number):
        env_width, env_height = map(int,input().split(" "))
        if env_height > card_height and env_width > card_width:
            data.append([env_width, env_height, idx+1])


    if len(data) == 0:
        print(0)
        return
    data.sort(key=lambda x: (x[0], -x[1]))

    # Apply a binary search LIS on heights
    # Apply a binary search LIS on heights
    height_lis: list[int] = []  # To store the longest increasing subsequence of heights
    pos = []  # To store the positions for reconstruction of the chain
    parent = [-1] * len(data)  # Parent array to reconstruct the path

    for idx, (_, hi, idx) in enumerate(data):
        # Find the position in the LIS where this height can be inserted
        pos_in_lis = bisect_left(height_lis, hi)

        # If pos_in_lis is equal to the length of lis, this means it extends the LIS
        if pos_in_lis == len(height_lis):
            height_lis.append(hi)
            pos.append(idx)
        else:
            height_lis[pos_in_lis] = hi
            pos[pos_in_lis] = idx

        # Track the parent to be able to reconstruct the sequence later
        if pos_in_lis > 0:
            parent[idx] = pos[pos_in_lis - 1]

    # The length of the LIS is the length of the largest chain
    max_chain_length = len(height_lis)

    # Reconstruct the chain of envelopes using the parent array
    chain = []
    current_pos = pos[-1]  # Start from the last position in the LIS
    while current_pos != -1:
        chain.append(data[current_pos][2])  # Add the original index of the envelope
        current_pos = parent[current_pos]

    # Reverse the chain to get it in the correct order
    chain.reverse()
    # Output the result
    print(max_chain_length)
    print(*chain)

if __name__ == "__main__":
    mysterious_problem()
