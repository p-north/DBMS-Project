import sqlite3


def connect_db():
    # Create and return the database connection
    conn = conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn


def register_for_event():

    # get event id
    event_id = input("\nEnter the ID of the event you want to register for: ")
    # get member id
    member_id = input("Enter your member ID: ")

    try:
        # connect to database
        conn = connect_db()
        # create cursour
        cursor = conn.cursor()

        # check if the event exists
        cursor.execute("SELECT 1 FROM event WHERE eventId = ?", (event_id,))
        if not cursor.fetchone():
            print("Error: Event not found")
            return

        # check if the member id exists
        cursor.execute("SELECT 1 FROM member WHERE memberID = ?", (member_id,))
        if not cursor.fetchone():
            print("Error: Member not found")
            return

        # check if already reserved
        cursor.execute("""
            SELECT 1 FROM reservations 
            WHERE memberId = ? AND itemId = ?
        """, (member_id, event_id))
        if cursor.fetchone():
            print("You're already registered for this event")
            return

        # registering the memberID by creating a reservation
        cursor.execute("""
            INSERT INTO reservations (memberId, itemId, reservationDate, status)
            VALUES (?, ?, date('now'), 'Confirmed')
        """, (member_id, event_id))
        conn.commit()
        print("Registration successful!")

    except sqlite3.Error as e:
        print(f"Error Registering for Event  {e}")
    finally:
        if conn:
            conn.close()


connect_db()
register_for_event()
