import sqlite3
from typing import List, Tuple, Optional

from resources import config


def insert_booking(booking_id: str, movie: str, seats: List[Tuple[int, int]]) -> None:
    """ Insert a new booking into the database."""
    seats_str = ','.join(f"{r}-{c}" for r, c in seats)
    with sqlite3.connect(config.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(config.CREATE_TABLE_QUERY)
        cur.execute(config.INSERT_QUERY,(booking_id, movie, seats_str))
        conn.commit()

def get_booking(booking_id: str) -> Optional[List[Tuple[int, int]]]:
    """ Retrieve booking by ID."""
    with sqlite3.connect(config.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(config.SELECT_QUERY, (booking_id,))
        result = cur.fetchone()
        if result:
            seats = [(int(p.split('-')[0]), int(p.split('-')[1])) for p in result[0].split(',')]
            return seats
    return None

def flush_bookings() -> None:
    """ Flush bookings when system is (re)started."""
    with sqlite3.connect(config.DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(config.DELETE_QUERY)
        conn.commit()
