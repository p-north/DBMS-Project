import sqlite3
import questionary
from setup_database import connect_db




def _register_for_event(member_id):
    print("\nEvent Registration")
    print("-----------------")

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
            print("No upcoming events available for registration")
            return

        print("\nUpcoming Events:")
        for event in events:
            print(f"[{event['eventId']}] {event['eventName']} ({event['date']} at {event['startTime']})")

        # Get event ID
        event_id = questionary.text("\nEnter event ID to register:").ask()

        # Validate event
        cursor.execute("SELECT eventName FROM event WHERE eventId = ?", (event_id,))
        event_data = cursor.fetchone()
        if not event_data:
            print("Error: Invalid event ID")
            return

        # Check if already registered
        cursor.execute("""
            SELECT 1 FROM reservations 
            WHERE memberId = ? AND itemId = ?
        """, (member_id, event_id))
        if cursor.fetchone():
            print("You're already registered for this event")
            return

        # Register for event
        cursor.execute("""
            INSERT INTO reservations (memberId, itemId, reservationDate, status)
            VALUES (?, ?, date('now'), 'Confirmed')
        """, (member_id, event_id))
        conn.commit()
        print(f"\nSuccess! You are now registered for {event_data['eventName']}.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def _view_event_registrations(member_id):
    print("\nYour Event Registrations")
    print("-----------------------")

    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT e.eventName, e.date, e.startTime, r.reservationDate, r.status 
            FROM reservations r
            JOIN event e ON r.itemId = e.eventId
            WHERE r.memberId = ? AND e.date >= date('now')
            ORDER BY e.date
        """, (member_id,))

        registrations = cursor.fetchall()
        
        if not registrations:
            print("You have no upcoming event registrations.")
            return

        print("\nYour Upcoming Events:")
        for i, reg in enumerate(registrations, 1):
            print(f"{i}. {reg['eventName']} ({reg['date']})")
            print(f"   Time: {reg['startTime']}")
            print(f"   Registered on: {reg['reservationDate']}")
            print(f"   Status: {reg['status']}\n")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()