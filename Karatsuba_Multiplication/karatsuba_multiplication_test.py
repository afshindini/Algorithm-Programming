"""Unit test for karatsuba_multiplication implementation"""
from typing import Any

from karatsuba_multiplication import karatsuba_recursive

tests = (
    (2, 3, 6),
    (1234, 5678, 7006652),
    (15, 75, 1125),
    (14785236, 25896314, 382883114020104),
    (45, 2, 90),
)

def check(test: Any) -> bool:
    """Function to compare the results of test function with ground truth data"""
    num1, num2, gt_sol = test
    code_sol = karatsuba_recursive(num1, num2)
    return gt_sol == code_sol

def test_karatsuba_recursive() -> None:
    """Unit test for karatsuba_recursive function"""
    assert check(tests[0])
    assert check(tests[1])
    assert check(tests[2])
    assert check(tests[3])
    assert check(tests[4])
