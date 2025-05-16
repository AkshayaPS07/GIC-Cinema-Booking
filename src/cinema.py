from src.utils.seating import SeatingManager
from src.utils.display import display_seating
from src.utils.helpers import generate_booking_id, parse_position
from src.db.database import insert_booking, get_booking, flush_bookings

class CinemaBookingSystem:
    """ Core class for handling seat booking operations."""

    def __init__(self, title: str, rows: int, cols: int) -> None:
        self.title = title
        self.seating = SeatingManager(rows, cols)
        self.booking_counter = 1

    def run(self) -> None:
        """ Start the booking interface loop."""
        while True:
            print(f"\nWelcome to GIC Cinemas")
            print(f"[1] Book tickets for {self.title} ({self.seating.available_seats()} seats available)")
            print("[2] Check bookings")
            print("[3] Exit")
            choice = input("Please enter your selection:\n> ").strip()
            if choice == '1':
                self.book_tickets()
            elif choice == '2':
                self.check_booking()
            elif choice == '3':
                print("Thank you for using GIC Cinemas system. Bye!")
                break

    def book_tickets(self) -> None:
        """ Handle ticket booking process."""
        while True:
            entry = input("\nEnter number of tickets to book, or enter blank to go back to main menu:\n> ").strip()
            if not entry:
                # Return to main menu if nothing is entered.
                return
            if not entry.isdigit() or int(entry) <= 0:
                # Check for invalid number
                print("Please enter a valid positive number.")
                continue
            num = int(entry)
            if num > self.seating.available_seats():
                print(f"Sorry, there are only {self.seating.available_seats()} seat(s) available.")
                continue
            break

        seats = self.seating.default_seat_selection(num)
        booking_id = generate_booking_id(self.booking_counter)
        self.booking_counter += 1
        print(f"\nSuccessfully reserved {num} {self.title} tickets.\nBooking id: {booking_id}\nSelected seats:")
        display_seating(self.seating.layout, seats, self.seating.cols)

        while True:
            custom = input("\nEnter blank to accept seat selection, or enter new seating position:\n> ").strip()
            if not custom:
                break
            new_start = parse_position(custom)
            if new_start:
                r, c = new_start
                custom_seats = self.seating.custom_seat_selection(r, c, num)
                if custom_seats:
                    seats = custom_seats
                    print(f"\nBooking id: {booking_id}\nSelected seats:")
                    display_seating(self.seating.layout, seats, self.seating.cols)
                else:
                    print("Not enough continuous seats from that position.")
            else:
                print("Invalid seat position format.")

        self.seating.reserved_seats(seats)
        insert_booking(booking_id, self.title, seats)
        print(f"\nBooking id: {booking_id} confirmed.")

    def check_booking(self) -> None:
        """ Allow user to retrieve a previous booking."""
        while True:
            booking_id = input("\nEnter booking id, or enter blank to go back to main menu:\n> ").strip().upper()
            if not booking_id:
                return
            seats = get_booking(booking_id)
            if seats:
                print(f"\nBooking id: {booking_id}\nSelected seats:")
                display_seating(self.seating.layout, seats, self.seating.cols)
            else:
                print("Booking ID not found.")
