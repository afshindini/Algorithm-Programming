"""Unit test for increasing subarray functions"""
from typing import Tuple
from increasing_subarray import count_long_subarray

tests = (
    (
        (2, 2, 4, 1, 4),
        2,
    ),
    (
        (7, 8, 5, 7, 7, 3, 2, 8),
        3,
    ),
    (
        (7, 7, 9, 1, 2, 11, 9, 6, 2, 8, 9),
        2,
    ),
    (
        (4, 18, 10, 8, 13, 16, 18, 1, 9, 6, 11, 13, 12, 5, 7, 17, 13, 3),
        1,
    ),
    (
        (11, 16, 10, 19, 20, 18, 3, 19, 2, 1, 8, 17, 7, 13, 1, 11, 1, 18, 19, 9, 7, 19, 24, 2, 12),
        4,
    ),
)

def check(test: Tuple) -> bool:
    """Check function to compare gt and calculated results"""
    data, ground_truth = test
    code_solution = count_long_subarray(data)
    return ground_truth == code_solution

def test_count_long_subarray() -> None:
    """Unit test for count_long_subarray function"""
    assert check(tests[0])
    assert check(tests[1])
    assert check(tests[2])
    assert check(tests[3])
    assert check(tests[4])
