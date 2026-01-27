import pytest

from codex_pr_demo import math_util


def test_add_returns_sum():
    assert math_util.add(2, 3) == 5


def test_divide_returns_quotient():
    assert math_util.divide(10, 2) == 5


def test_divide_raises_on_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        math_util.divide(5, 0)
