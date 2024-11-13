"""This is a solution for mysterious problem"""


def mysterious_problem() -> None:
    """Print the order of envelop and its increasing indices"""
    env_number, card_width, card_height = map(int,input().split(" "))
    data = []
    for idx in range(env_number):
        env_width, env_height = map(int,input().split(" "))
        if env_height > card_height and env_width > card_width:
            data.append([env_width, env_height, idx+1])

    data.sort(key=lambda x: (x[0], -x[1]))
    if len(data) == 0:
        print(0)
        return
    dp = [1] * len(data)

    results = [[data[idx][2]] for idx in range(len(data))]
    for idx,_ in enumerate(data):
        for prev_id in range(idx):
            temp = []
            if data[prev_id][0] < data[idx][0] and data[prev_id][1] < data[idx][1]:
                if dp[idx] < dp[prev_id]+1:
                    temp = results[prev_id].copy()
                    temp.append(data[idx][2])
                    results[idx] = temp
                dp[idx] = max(dp[idx],dp[prev_id]+1)

    print(max(dp))
    print(*results[dp.index(max(dp))])



if __name__ == "__main__":
    mysterious_problem()
