"""This is a solution for hulk problem"""

def hulk() -> str:
    """return rhe expression in string"""
    number = int(input())
    data = ["I hate ", "I love "]
    return "".join([ data[rep%2] if rep<1 else "that "+data[rep%2] for rep in range(number)]+["it"])



if __name__ == "__main__":
    print(hulk())
