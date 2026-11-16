
from hypothesis import given, strategies as st

from restaurant_bill_parser import (
    clean_dish_name,
    parse_item_prices,
    split_amount,
)

@given(st.one_of(st.text(), st.none()))
def test_clean_dish_name_no_crash(value):
    """Test dish-name cleaning with random strings and None."""
    try:
        result = clean_dish_name(value)
    except Exception as exc:
        assert False, (
            f"clean_dish_name crashed for input {value!r}: "
            f"{type(exc).__name__}: {exc}"
        )

    assert isinstance(result, str)
    assert not any(marker in result for marker in ("*", "#", "~"))

@given(st.one_of(st.text(), st.none()))
def test_parse_item_prices_no_crash(value):
    """Test price parsing with random strings and None."""
    try:
        result = parse_item_prices(value)
    except Exception as exc:
        assert False, (
            f"parse_item_prices crashed for input {value!r}: "
            f"{type(exc).__name__}: {exc}"
        )

    assert isinstance(result, list)
    assert all(type(price) is int and price >= 0 for price in result)

@given(st.one_of(st.text(), st.none()))
def test_split_amount_no_crash(value):
    """Test bill splitting with random strings and None."""
    try:
        result = split_amount(value)
    except Exception as exc:
        assert False, (
            f"split_amount crashed for input {value!r}: "
            f"{type(exc).__name__}: {exc}"
        )

    assert type(result) is int
    assert result >= 0