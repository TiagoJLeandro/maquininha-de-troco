import pytest
from calculate_change import calculate_change


default_coins_list = [
            200, 100, 50, 20, 10, 5, 
            2, 1, 0.5, 0.25, 0.10, 0.05, 0.01
]

@pytest.mark.parametrize('prod_value,received,expected',
                        [(100, 0, []),
                         (388.91, 777.82, [1,1,1,1,1,1,1,1,1,1,1,1,1]),
                         (0.10, 0.14, [0,0,0,0,0,0,0,0,0,0,0,0,4]),
                         (0.10, 0.16, [0,0,0,0,0,0,0,0,0,0,0,1,1]),
                         (0, 200, [1,0,0,0,0,0,0,0,0,0,0,0,0]),
                         (0, 100, [0,1,0,0,0,0,0,0,0,0,0,0,0]),
                         (0, 50, [0,0,1,0,0,0,0,0,0,0,0,0,0]),
                         (0, 20, [0,0,0,1,0,0,0,0,0,0,0,0,0]),
                         (0, 10, [0,0,0,0,1,0,0,0,0,0,0,0,0]),
                         (0, 5, [0,0,0,0,0,1,0,0,0,0,0,0,0]),
                         (0, 2, [0,0,0,0,0,0,1,0,0,0,0,0,0]),
                         (0, 1, [0,0,0,0,0,0,0,1,0,0,0,0,0]),
                         (0, 0.5, [0,0,0,0,0,0,0,0,1,0,0,0,0]),
                         (0, 0.25, [0,0,0,0,0,0,0,0,0,1,0,0,0]),
                         (0, 0.10, [0,0,0,0,0,0,0,0,0,0,1,0,0]),
                         (30.80, 50.80, [0,0,0,1,0,0,0,0,0,0,0,0,0])

    ]
)
def test_if_change_was_decomposed(prod_value, received, expected):
    assert calculate_change(
        default_coins_list, prod_value, received) == expected
