# GIC Cinemas Booking System.

A command-line cinema booking system.

## Ticket Booking
When user selects [1], the booking "workflow" should start. User needs to input the desired number of tickets they want to book. If there are not enough seats available, user should be allowed to try again.

After seats are allocated, a booking id should be generated and displayed along with the number of tickets booked and the seating map showing default selected seats. The seats reserved for the current booking should be marked differently than seats taken by existing bookings.

Use the following rules for default seat selection:
* Start from furthest row from the screen.
* Start from the middle-most possible col.
* When a row is not enough to accomodate the number of tickets, it should overflow to the next row closer to the screen.

User can choose another seating position by specifying the starting position of the seats. Seating assignment should follow this rule:
* Starting from the specified position, fill up all empty seats in the same row all the way to the right of the cinema hall.
* When there is not enough seats available, it should overflow to the next row closer to the screen.
* Seat allocation for overflow follows the rules for default seat selection.

## Project Structure
```
resources/
    config.py
src/
  main.py
  cinema.py
  db/
    database.py
  utils/
    helpers.py
    display.py
    seating.py
tests/
  test_helpers.py
pyproject.toml ( for requirements management)
```

## Requirements
- Python 3.7+
- pytest (for testing)

## Run Application
```bash
python src/main.py
```

## Run Tests
```bash
pytest tests/
```