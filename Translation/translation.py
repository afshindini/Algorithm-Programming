"""This is a solution for translation problem"""

def translation() -> str:
    """return YES if the translation is tru else return NO"""
    original = input("Enter the main word: ")
    translated = input("Enter the translated word: ")
    if original[::-1] == translated:
        return "YES"
    return "NO"



if __name__ == "__main__":
    print(translation())
