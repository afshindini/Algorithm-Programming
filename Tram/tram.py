"""This is a solution for tram problem"""

def tram() -> int:
    """Returns minimum capcity of the tram"""
    station_number = int(input())
    passengers, capacity = 0, 0
    for _ in range(station_number-1):
        exit_pass, enter_pass = map(int, input().split(" "))
        passengers = passengers + (enter_pass - exit_pass)
        capacity = max(capacity, passengers)
    return capacity



if __name__ == "__main__":
    print(tram())
