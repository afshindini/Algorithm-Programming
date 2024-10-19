"""Team problem"""

def team_decision() -> int:
    """Return the number of solved solutions by the team"""
    result = 0
    num = int(input("Enter the number of problems: "))
    while num>0:
        if input("Enter results separated by space:").count("1")>1:
            result +=1
        num -=1
    return result

if __name__ == "__main__":
    print(team_decision())
