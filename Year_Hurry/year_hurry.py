"""This is a solution for the new and hurry problem"""

def year_hurry() -> int:
    """Return the number of problems he can solve"""
    problems, travel_time = map(int, input().split(" "))
    problem_time = 240 - travel_time
    for num in range(problems, 0, -1):
        if num * (num + 1) <= problem_time*0.4:
            return num
    return 0


if __name__ == "__main__":
    print(year_hurry())
