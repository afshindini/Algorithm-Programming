"""This is a solution for the Borze problem"""

def borze() -> str:
    """Return the decoded string"""
    coded = input()
    result = []
    idx = 0
    while idx < len(coded):
        if coded[idx] == '.':
            idx +=1
            result.append('0')
        elif coded[idx:idx+2] == "--":
            idx+=2
            result.append('2')
        else:
            idx+=2
            result.append('1')
    return ''.join(result)

if __name__ == "__main__":
    print(borze())
