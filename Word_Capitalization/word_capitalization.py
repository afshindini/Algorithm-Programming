"""This is a solution for word capitalization problem"""


def word_capitalization() -> str:
    """Return the first letter in uppercase and keep other ones unchanged"""
    word = input()
    
    return word[0].upper() + word[1:]



if __name__ == "__main__":
    print(word_capitalization())
    