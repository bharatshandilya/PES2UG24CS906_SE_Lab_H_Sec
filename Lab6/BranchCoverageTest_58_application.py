import pytest

from restaurant_bill import bill_total, split_bill, table_wait


# bill_total: cover both outcomes of each condition

def test_unknown_section():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("invalid", 100, 2, False)


def test_valid_section():
    assert bill_total("dine_in", 100, 2, False) == 115


def test_invalid_order_negative_food():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -1, 2, False)


def test_invalid_order_zero_guests():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", 100, 0, False)


def test_valid_order():
    assert bill_total("takeaway", 100, 1, False) == 105


def test_happy_hour_applies():
    assert bill_total("dine_in", 100, 2, True) == 92


def test_happy_hour_not_applied():
    assert bill_total("dine_in", 100, 2, False) == 115


def test_takeaway_excluded_from_happy_hour():
    assert bill_total("takeaway", 100, 2, True) == 105


def test_large_party_service_charge():
    assert bill_total("rooftop", 100, 8, False) == 330


def test_small_party_no_extra_charge():
    assert bill_total("rooftop", 100, 7, False) == 120


# split_bill: validation and both rounding outcomes

def test_invalid_people_count():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(100, 0, 0)


def test_valid_people_count():
    assert split_bill(100, 2, 0) == 50


def test_negative_tip():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(100, 2, -1)


def test_valid_tip():
    assert split_bill(100, 2, 10) == 55


def test_split_with_remainder():
    assert split_bill(100, 3, 0) == 34


def test_split_without_remainder():
    assert split_bill(100, 2, 0) == 50


# table_wait: cover every seating decision

def test_party_too_large():
    assert table_wait(13, 5, False) == "call ahead"


def test_reservation_takes_priority():
    assert table_wait(4, 0, True) == "seat now"


def test_no_tables_available():
    assert table_wait(4, 0, False) == "waitlist"


def test_large_party_and_one_table():
    assert table_wait(7, 1, False) == "waitlist"


def test_large_party_and_two_tables():
    assert table_wait(7, 2, False) == "seat now"


def test_small_party_and_available_table():
    assert table_wait(4, 1, False) == "seat now"
