"""Karatsuba Multiplication algorithm for n^2-digit numbers"""
def karatsuba_recursive(number1: int,number2: int) -> int:
    """Recursive algorithm for Karatsuba multiplication"""
    len1 = len(str(number1))
    len2 = len(str(number2))
    power = max(len1,len2)
    if len1 == 1 or len2 == 1:
        out = number1 * number2
    else:
        num1_left = int(str(number1)[:len1//2])
        num1_right = int(str(number1)[len1//2:])
        num2_left = int(str(number2)[:len2//2])
        num2_right = int(str(number2)[len2//2:])
        left_multi = karatsuba_recursive(num1_left,num2_left)
        right_multi = karatsuba_recursive(num1_right,num2_right)

        out = (10**int(power)) * left_multi + (10**int(power/2)) \
            * ((num1_left + num1_right) * (num2_left + num2_right) \
            - left_multi - right_multi) + (right_multi)

    return int(out)

if __name__ == '__main__':
    num1 = int(input("Insert the first n^2-digit number: "))
    num2 = int(input("Insert the second n^2-digit number: "))
    output = karatsuba_recursive(num1,num2)
    print("The multiplication result is: ", output)
