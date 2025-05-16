from src.utils.helpers import generate_booking_id, parse_position

def test_generate_booking_id():
    assert generate_booking_id(1) == "GIC0001"
    assert generate_booking_id(25) == "GIC0025"

def test_parse_position():
    assert parse_position("A1") == (0, 0)
    assert parse_position("C5") == (2, 4)
    assert parse_position("Z50") == (25, 49)
    assert parse_position("invalid") is None