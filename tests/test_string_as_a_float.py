from random import randint
import pytest
from string_as_a_float import string_as_a_float


randint_ = str(randint(0, 9999))

@pytest.mark.parametrize('given,expected',
                        [("111a", '111'),
                         ('a111', '111'),
                         ('1fsdf3sf3', '133'),
                         ('1152asdasd.asdasd', '1152.'),
                         ('asda' + randint_ + "asd", randint_),
                         (',,,,12.,,.10..', '12.10')
    ]
)
def test_if_only_str_like_floats_will_be_returned(given, expected):
    assert string_as_a_float(given) == string_as_a_float(expected)

@pytest.mark.parametrize('given,expected',
                        [("111111", '1111.11'),
                         ('2515544', '2515.54'),
                         ('0.00000545751', '0.00'),
                         ('00123da584.45wr85', '0012.35')
    ]
)
def test_if_only_two_decimal_places_were_returned(given, expected):
     assert string_as_a_float(given) == string_as_a_float(expected)
