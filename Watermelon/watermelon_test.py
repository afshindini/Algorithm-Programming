"""Unit test for watermelon functions"""

from watermelon import watermelon1, watermelon2


def test_watermelon1() -> None:
    """Unit test for watermelon1 function"""
    assert watermelon1(5)=='NO'
    assert watermelon1(20)=='YES'
    assert watermelon1(368)=='YES'
    assert watermelon1(719)=='NO'
    assert watermelon1(545678)=='YES'

def test_watermelon2() -> None:
    """Unit test for watermelon1 function"""
    assert watermelon2(5)=='NO'
    assert watermelon2(20)=='YES'
    assert watermelon2(368)=='YES'
    assert watermelon2(719)=='NO'
    assert watermelon2(545678)=='YES'
