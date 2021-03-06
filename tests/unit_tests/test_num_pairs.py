import pytest
from pbc.tools import number_pairs


test_data = [
    pytest.param((4.5, 5.5), 1, id='float'),
    pytest.param(('string1', 'string2'), 0, id="strings don't create pair"),
    pytest.param((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, -3, -3, 3.0, 3.123, "asdasd"), 6, id='mixed data types'),
    pytest.param((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 5, id='numbers from 1 to 10'),
]

@pytest.mark.pairs
@pytest.mark.parametrize('sequence, expected', test_data)
def test_input(sequence, expected):
    assert len(number_pairs(*sequence)) == expected


