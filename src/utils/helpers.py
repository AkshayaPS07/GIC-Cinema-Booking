import string
from typing import Optional, Tuple

def generate_booking_id(n: int) -> str:
    """ Generate formatted booking ID. Eg: GIC000n"""
    return f"GIC{n:04d}"

def parse_position(pos: str) -> Optional[Tuple[int, int]]:
    """ Parse seat position to row-col index."""
    if len(pos) < 2:
        return None
    row_char = pos[0].upper()
    if row_char not in string.ascii_uppercase[:26]:
        return None
    try:
        col = int(pos[1:]) - 1
    except ValueError:
        return None
    row = ord(row_char) - ord('A')
    return (row, col)
