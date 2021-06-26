import pytest


@pytest.mark.parametrize("test_input, expected", [(1,1), (2,4), (3,9), (4,16)])
def test_squares(test_input, expected):
    assert (test_input * test_input) == expected
