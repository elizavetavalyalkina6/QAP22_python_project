import pytest
from format_price import format_price


@pytest.mark.parametrize(
    "price, res",
    [
        ("1234", "1 234.00"),
        ("3456789.2", "3 456 789.20"),
        ("66.997654321", "67.00"),
        ("99.99999", "100.00"),
        ("0.0019", "0.00"),
        ("6238.9", "6 238.90"),
        ("0.999", "1.00"),
        ("876 945 432.60", "876 945 432.60"),
        ("0", "0.00"),
        ("-2804", "-2 804.00"),
        ("-0.999", "-1.00"),
        ("abc", "abc"),
        ("None", "None"),
    ],
)
def test_format_price(price, res):
    assert format_price(price) == res
