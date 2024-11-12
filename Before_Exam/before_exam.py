"""This is a solution for before an exam problem"""


def before_exam() -> None:
    """Print any valid schedule of studying based on rules"""
    day_hours = list(map(int,input("Enter number of days and total hours of study: ").split(" ")))
    data = []
    results = []
    low, high = 0, 0
    for _ in range(day_hours[0]):
        low_high = list(map(int,input("Enter low and high hour limits per days: ").split(" ")))
        low += low_high[0]
        high += low_high[1]
        data.append(low_high)
        results.append(low_high[0])
    if day_hours[1] > high or day_hours[1] < low:
        print("NO")
        return
    idx = len(data) - 1
    while(sum(results) != day_hours[1] and idx >=0):
        results[idx] = day_hours[1] - sum(results)+ results[idx] \
            if day_hours[1] - sum(results) + results[idx] <= data[idx][1] else data[idx][1]
        idx -= 1
    print("YES")
    print(*results)


if __name__ == "__main__":
    before_exam()
    