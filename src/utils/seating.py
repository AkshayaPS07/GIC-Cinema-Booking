from typing import List, Tuple

class SeatingManager:
    """Manages seat availability and allocation."""

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.layout: List[List[str]] = [['.' for _ in range(cols)] for _ in range(rows)]

    def available_seats(self) -> int:
        """ Return count of available seats."""
        return sum(row.count('.') for row in self.layout)

    def reserved_seats(self, seats: List[Tuple[int, int]]) -> None:
        """ Mark given seats as reserved."""
        for r, c in seats:
            self.layout[r][c] = '#'

    def default_seat_selection(self, num: int) -> List[Tuple[int, int]]:
        """ Automatically choose seats starting from back and center."""
        for row in reversed(range(self.rows)):
            # To get the middle of the column.
            start = (self.cols - num) // 2
            for col in range(start, self.cols - num + 1):
                if all(self.layout[row][col + i] == '.' for i in range(num)):
                    return [(row, col + i) for i in range(num)]
        return self.overflow_selection(num)

    def overflow_selection(self, num: int) -> List[Tuple[int, int]]:
        """ Fallback seat selection logic when no row fits all."""
        seats = []
        for row in reversed(range(self.rows)):
            for col in range(self.cols):
                if self.layout[row][col] == '.':
                    seats.append((row, col))
                    if len(seats) == num:
                        return seats
        return []

    def custom_seat_selection(self, row: int, col: int, num: int) -> List[Tuple[int, int]]:
        """ Seat selection from a given starting point."""
        seats = []
        for r in range(row, -1, -1):
            while col < self.cols and len(seats) < num:
                if self.layout[r][col] == '.':
                    seats.append((r, col))
                else:
                    return []
                col += 1
            if len(seats) == num:
                return seats
            col = 0
        return []
