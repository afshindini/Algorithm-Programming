"""This is a solution for beautiful matrix problem"""

def beautiful_matrix() -> int:
    """Return the number of moves to make matrix beautiful"""
    row_id, col_id = 0, 0
    for idx in range(5):
        row = input("Elements of the one row but 5 times separated by comma: ").split(" ")
        if '1' in row:
            row_id =  idx + 1
            col_id = row.index('1') + 1
    return abs(3 - row_id) + abs(3 - col_id)


if __name__ == "__main__":
    print(beautiful_matrix())
    