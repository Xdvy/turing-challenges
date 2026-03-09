import pytest
from itertools import islice
from turing_challenges.challenge_001.challenge import (
  multiples_five_and_seven_below_value,
  compute_sum_multiples_five_and_seven_below_value,
  Challenge001,
)

@pytest.mark.parametrize(
    "max_value,expected",
    [
        (20, [5,7,10,14,15]),
        (10, [5,7]),
        (5, []),
        (1, []),
        (-20, []),
    ],
)
def test_multiples_five_and_seven_below_value(max_value, expected):
  assert list(multiples_five_and_seven_below_value(max_value)) == expected

@pytest.mark.parametrize(
    "max_value,expected",
    [
        (20, 51),
        (10, 12),
        (5, 0),
        (1, 0),
        (-20, 0),
    ],
)
def test_compute_sum_multiples_five_and_seven_below_value(max_value, expected) :
  assert compute_sum_multiples_five_and_seven_below_value(max_value) == expected

def test_large_input_generator():
    gen = multiples_five_and_seven_below_value(10_000_000)
    assert list(islice(gen, 5)) == [5,7,10,14,15]

# -------------------
# Tests erreurs Classe
# -------------------

@pytest.fixture
def challenge():
    return Challenge001()

def test_challenge_solve(challenge,max_value=20) :
   assert challenge.solve(max_value) == 51
