from src.cinema import CinemaBookingSystem
from src.db.database import flush_bookings


def main() -> None:
    """ Main entry point to launch the Cinema Booking System."""
    print("Please define movie title and seating map in [Title] [Row] [SeatsPerRow] format:")
    while True:
        init = input("> ").strip()
        try:
            title, rows, seats = init.rsplit(" ", 2)
            rows, seats = int(rows), int(seats)
            if 1 <= rows <= 26 and 1 <= seats <= 50:
                break
            else:
                print("Row max allowed = 26, Seats per row max allowed= 50.")
        except Exception:
            print("Invalid format. Use: [Title] [Row] [SeatsPerRow]")

    system = CinemaBookingSystem(title, rows, seats)
    system.run()

if __name__ == "__main__":
    flush_bookings()
    main()
