import pytest

from restaurant_bill import bill_total, split_bill, table_wait


# bill_total(): valid orders and pricing rules

def test_dine_in_bill():
    assert bill_total("dine_in", 1000, 2, False) == 1155


def test_takeaway_bill():
    assert bill_total("takeaway", 500, 2, False) == 525


def test_takeaway_happy_hour_does_not_discount():
    assert bill_total("takeaway", 500, 2, True) == 525


def test_rooftop_happy_hour_large_party():
    assert bill_total("rooftop", 1000, 8, True) == 1176


def test_happy_hour_dine_in():
    assert bill_total("dine_in", 1000, 2, True) == 924


def test_zero_food_total():
    assert bill_total("dine_in", 0, 1, False) == 0


def test_unknown_section_raises_error():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("garden", 500, 2, False)


def test_negative_food_total_raises_error():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -100, 2, False)


def test_zero_guests_raises_error():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", 500, 0, False)


# split_bill(): valid splits and input validation

def test_even_split():
    assert split_bill(1000, 4, 10) == 275


def test_split_with_remainder_rounds_up():
    assert split_bill(100, 3, 0) == 34


def test_split_without_tip():
    assert split_bill(600, 3, 0) == 200


def test_zero_people_raises_error():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(1000, 0, 10)


def test_negative_tip_raises_error():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(1000, 2, -5)


# table_wait(): seating decisions

def test_party_over_twelve_must_call_ahead():
    assert table_wait(13, 5, False) == "call ahead"


def test_reservation_seated_immediately():
    assert table_wait(4, 0, True) == "seat now"


def test_no_free_tables_means_waitlist():
    assert table_wait(4, 0, False) == "waitlist"


def test_large_party_with_one_table_waitlists():
    assert table_wait(7, 1, False) == "waitlist"


def test_large_party_with_two_tables_is_seated():
    assert table_wait(7, 2, False) == "seat now"


def test_small_party_with_available_table_is_seated():
    assert table_wait(4, 1, False) == "seat now"
