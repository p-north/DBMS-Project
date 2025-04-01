# DB Schema
import sqlite3
from setup_database import connect_db

def find_event(search_term=None):
    conn = connect_db()
    cursor = conn.cursor()

    if search_term:
        # Search with term
        cursor.execute('''
            SELECT eventId, eventName, eventType, date, startTime, endTime,
                   targetAudience, description, roomId
            FROM event
            WHERE (eventName LIKE ? OR date = ?)
                  AND date >= date('now')
            ORDER BY date
        ''', ('%' + search_term + '%', search_term))
    else:
        # Show all upcoming events
        cursor.execute('''
            SELECT eventId, eventName, eventType, date, startTime, endTime,
                   targetAudience, description, roomId
            FROM event
            WHERE date >= date('now')
            ORDER BY date
        ''')

    events = cursor.fetchall()
    conn.close()

    if not events:
        print("\nNo events found")
        return

    print(f"\nFound {len(events)} events:")
    for event in events:
        print(f"\nEvent ID: {event[0]}")
        print(f"Name: {event[1]}")
        print(f"Type: {event[2]}")
        print(f"Date: {event[3]}")
        print(f"Time: {event[4]} - {event[5]}")
        print(f"Audience: {event[6]}")
        print(f"Description: {event[7]}")
        print(f"Room: {event[8]}")
        print("-" * 40)


