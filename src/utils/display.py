from typing import List, Tuple

def display_seating(layout: List[List[str]], selected: List[Tuple[int, int]], cols: int) -> None:
    """ Render the seat map with selected indicators."""
    screen_line = "S C R E E N"
    print(f"\n{'  ' * int(cols-12//2)}{screen_line}{'  ' * int(cols-12//2)}\n{' - ' * (cols)}")
    mark = [[c for c in row] for row in layout]
    for r, c in selected:
        mark[r][c] = 'o'
    for i, row in enumerate(mark):
        print(f"{chr(ord('A')+i)}  " + '  '.join(row))
    print("  " + ' '.join(f"{i+1:>2}" for i in range(cols)))
