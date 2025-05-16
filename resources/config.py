DB_PATH = "gic_cinemas.db"

CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS bookings (id TEXT PRIMARY KEY, movie TEXT, seats TEXT)"
INSERT_QUERY = "INSERT INTO bookings (id, movie, seats) VALUES (?, ?, ?)"
SELECT_QUERY = "SELECT seats FROM bookings WHERE id = ?"
DELETE_QUERY = "DELETE FROM bookings"