import sqlite3


def connect_db():
    # Create and return the database connection
    conn = conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn


def volunteer_for_event():
    print("\nEvent Volunteer Signup")
    print("---------------------")

    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Show upcoming events
        cursor.execute("""
            SELECT eventId, eventName, date, startTime 
            FROM event 
            WHERE date >= date('now')
            ORDER BY date
        """)

        events = cursor.fetchall()
        if not events:
            print("No upcoming events available for volunteering")
            return

        print("\nUpcoming Events:")
        for event in events:
            print(
                f"[{event['eventId']}] {event['eventName']} ({event['date']} at {event['startTime']})")

        # Get volunteer details
        event_id = input("\nEnter event ID to volunteer for: ")
        member_id = input("Enter your member ID: ")
        role = input("Enter preferred volunteer role: ")

        # Validate inputs
        cursor.execute("SELECT 1 FROM event WHERE eventId = ?", (event_id,))
        if not cursor.fetchone():
            print("Error: Invalid event ID")
            return

        cursor.execute(
            "SELECT firstName, lastName FROM member WHERE memberID = ?", (member_id,))
        member = cursor.fetchone()
        if not member:
            print("Error: Invalid member ID")
            return

        # Check for existing signup
        cursor.execute("""
            SELECT 1 FROM volunteer
            WHERE eventID = ? AND memberID = ?
        """, (event_id, member_id))
        if cursor.fetchone():
            print("You're already signed up to volunteer for this event")
            return

        # Register volunteer
        cursor.execute("""
            INSERT INTO volunteer (eventID, memberID, role)
            VALUES (?, ?, ?)
        """, (event_id, member_id, role))

        conn.commit()
        print(
            f"\nSuccess! {member['firstName']} {member['lastName']} is now signed up as a {role} for this event.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()


connect_db()
volunteer_for_event()
