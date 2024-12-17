"""This is a solution for fox and snake problem"""

def fox_snake() -> None:
    """Draw the snake"""
    n_row, m_col = map(int, input().split(" "))
    for row in range(n_row):
        if row %2 == 0:
            print(m_col * "#")
        else:
            if row % 4 == 1:
                print((m_col-1)*'.' + "#")
            if row % 4 == 3:
                print("#" + (m_col-1)*'.')


if __name__ == "__main__":
    fox_snake()
