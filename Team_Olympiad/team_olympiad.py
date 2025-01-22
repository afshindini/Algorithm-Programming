"""This is a solution for the Team Olympiad problem"""

def team_olympiad() -> None:
    """Print the minimum number of possible teams"""
    _ = int(input())
    skills = list(map(int, input().split(" ")))
    math = [idx for idx, elem in enumerate(skills) if elem == 1]
    program = [idx for idx, elem in enumerate(skills) if elem == 2]
    physical = [idx for idx, elem in enumerate(skills) if elem == 3]
    teams = min(len(math), len(program), len(physical))
    print(teams)
    if teams !=0:
        for idx in range(teams):
            print(*[math[idx]+1, program[idx]+1, physical[idx]+1])


if __name__ == "__main__":
    team_olympiad()
    