import pytest

from test_ci import sum_my


@pytest.mark.parametrize("a, b, result", [(1, 2, 3), (2, 3, 4)])
def test_sum_my(a, b, result):
    assert sum_my(a, b) == result