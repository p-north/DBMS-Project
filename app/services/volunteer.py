import sqlite3
import questionary
from setup_database import connect_db

def volunteer_for_event(loginID, eventID=None):
    print("\nEvent Volunteer Signup")
    print("---------------------")

    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
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
            input("\nPress Enter to return to the menu...")
            return

        print("\nUpcoming Events:")
        for event in events:
            print(f"[{event['eventId']}] {event['eventName']} ({event['date']} at {event['startTime']})")

        # Get event ID if not provided
        if eventID is None:
            event_id = questionary.text("\nEnter event ID to volunteer for:").ask()
        else:
            event_id = eventID

        # Validate event
        cursor.execute("SELECT eventName FROM event WHERE eventId = ?", (event_id,))
        event_data = cursor.fetchone()
        if not event_data:
            print("Error: Invalid event ID")
            input("\nPress Enter to return to the menu...")
            return

        # Get role
        role = questionary.text("Enter preferred volunteer role:").ask()

        # Check member exists
        cursor.execute(
            "SELECT firstName, lastName FROM member WHERE memberID = ?", (loginID,))
        member = cursor.fetchone()
        if not member:
            print("Error: Invalid member ID")
            input("\nPress Enter to return to the menu...")
            return

        # Check for existing signup
        cursor.execute("""
            SELECT 1 FROM volunteer
            WHERE eventID = ? AND memberID = ?
        """, (event_id, loginID))
        if cursor.fetchone():
            print("You're already signed up to volunteer for this event")
            input("\nPress Enter to return to the menu...")
            return

        # Register volunteer
        cursor.execute("""
            INSERT INTO volunteer (eventID, memberID, role)
            VALUES (?, ?, ?)
        """, (event_id, loginID, role))

        conn.commit()
        print(f"\nSuccess! {member['firstName']} {member['lastName']} is now signed up as a {role} for {event_data['eventName']}.")
        input("\nPress Enter to return to the menu...")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        input("\nPress Enter to return to the menu...")
    finally:
        if conn:
            conn.close()


