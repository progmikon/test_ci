import pytest

from test_ci import sum_my, multiply_my, dev


@pytest.mark.parametrize("a, b, result", [(1, 2, 3), (2, 3, 5)])
def test_sum_my(a, b, result):
    assert sum_my(a, b) == result

@pytest.mark.parametrize("a, b, result", [(1, 2, 2), (2, 3, 6)])
def test_multiply(a, b, result):
    assert multiply_my(a, b) == result

@pytest.mark.parametrize("a, b, result", [(2, 1, 2), (6, 3, 2)])
def test_dev(a, b, result):
    assert dev(a, b) == result