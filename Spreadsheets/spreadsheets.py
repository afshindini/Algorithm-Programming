"""This is a solution to spreadsheet problem"""



letter_int = {chr(val):idx+1 for idx,val in enumerate(range(65, 91))}
int_letter = {idx:chr(val) for idx,val in enumerate(range(65, 91))}


def bc_to_rc_converter(string: str) -> int:
    """Convert column values from AA to RC crds"""
    result = 0
    for idx,val in enumerate(string):
        result += 26**(len(string)-1-idx)*letter_int[val]
    return int(result)


def rc_to_bc_converter(number: int, val:int) -> str:
    """Convert column values from RC to AA crds"""
    number -=1
    if number//val == 0:
        return int_letter[int(number)]
    temp = rc_to_bc_converter(int(number//val), val)
    return temp + int_letter[int(number%val)]


def spreadsheet() -> None:
    """print the converted postion in another system"""
    number = int(input().strip())
    solution = []
    for _ in range(number):
        crd = input().strip()
        if crd[0] == 'R' and crd[1].isdigit() and 'C' in crd:
            c_index = crd.index('C')
            row = int(crd[1:c_index])
            column = int(crd[c_index + 1:])
            solution.append(f"{rc_to_bc_converter(column, 26)}{row}")
        else:
            temp = 0
            while temp < len(crd) and crd[temp].isalpha():
                temp += 1
            col = crd[:temp]
            row = int(crd[temp:])
            solution.append(f"R{row}C{bc_to_rc_converter(col)}")

    for val in solution:
        print(val)



if __name__ == "__main__":
    spreadsheet()