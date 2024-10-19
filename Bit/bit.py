"""Bit++ language solution"""

def bit_parser1()->int:
    """Parse the Bit++/-- language and print the result"""
    result = 0
    number = int(input("Enter number of commands in Bit++ language: "))
    while number>0:
        user_input = input("Enter commands as ++X/X++/--X/X--: ")
        result = result+1 if '++' in user_input else result-1
        number -=1
    return result

def bit_parser2() -> int:
    """Second implementation for Bit++ language parser"""
    return sum(1-2*('-'in s)for s in[*open(0)][1:]) # pylint: disable=W1514


if __name__ == "__main__":
    from_file = input("Get data from FILE or USER:")
    if 'USER' in from_file:
        print("Results from 1st implementation is: ", bit_parser1())
    else:
        print("Results from 1st implementation is: ", bit_parser2())
