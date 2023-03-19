from hypothesis import given
from hypothesis.strategies import integers, lists, sets

import a2_part2_q1_q2 as a


def mystery_1a_nested(x: int, y: set[int]) -> str:
    """Mystery 1a."""
    if len(y) > 1 and x <= 0:
        return 'David'
    else:
        if x > 1 and sum({n ** 2 for n in y}) >= 10:
            return 'Mario'
        else:
            return 'David'


def mystery_1b_nested(n: int, rows_of_nums: list[list[int]]) -> int:
    """Mystery 1b."""
    if len(rows_of_nums) > n > 0:
        if n == 1:
            return 0
        elif n in rows_of_nums[n]:
            return sum(rows_of_nums[n]) + n
        else:
            return sum(rows_of_nums[0])
    else:
        if len(rows_of_nums) > 20:
            return 20
        else:
            return n


def mystery_2a_if(x: int, y: int, z: set[int]) -> bool:
    """Mystery 2a."""
    if x >= y:
        if x in z:
            return True
        elif y not in z:
            return False
        else:
            return False
    else:
        if x in z:
            return False
        elif y not in z:
            return True
        else:
            return False


def mystery_2b_if(n: int) -> bool:
    """Mystery 2b."""
    if n % 2 == 0:
        if n % 3 == 1:
            return True
        else:
            return False
    elif n <= 4:
        if n < 0:
            return True
        else:
            return False
    else:
        if n % 3 == 1:
            return False
        else:
            return True


def mystery_2c_if(c1: int, c2: int, c3: int) -> bool:
    """Mystery 2c."""
    if c1 == c2:
        return False
    elif c1 > c2:
        if c3 <= c2:
            return False
        else:
            return True
    else:
        if c2 < c3:
            return True
        else:
            return False


@given(x=integers(), y=sets(integers()))
def test_1a(x: int, y: set[int]) -> None:
    assert a.mystery_1a_flat(x, y) == mystery_1a_nested(x, y)


@given(x=integers(), rows_of_nums=lists(lists(integers())))
def test_1b(x: int, rows_of_nums: [list[list[int]]]) -> None:
    assert a.mystery_1b_flat(x, rows_of_nums) == mystery_1b_nested(x, rows_of_nums)


@given(x=integers(), y=integers(), z=sets(integers()))
def test_2a(x: int, y: int, z: set[int]) -> None:
    assert a.mystery_2a_no_if(x, y, z) == mystery_2a_if(x, y, z)


@given(n=integers())
def test_2b(n: int) -> None:
    assert a.mystery_2b_no_if(n) == mystery_2b_if(n)


@given(c1=integers(), c2=integers(), c3=integers())
def test_2c(c1: int, c2: int, c3: int) -> None:
    assert a.mystery_2c_no_if(c1, c2, c3) == mystery_2c_if(c1, c2, c3)


if __name__ == '__main__':
    import pytest
    pytest.main(['test.py', '-v'])
