# DB Schema
import sqlite3


def connect_db():
    # Create and return the database connection
    conn = conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn


def find_event(detailed=True):
    search_term = input("Search by event name or date (YYYY-MM-DD): ")

    # connec tto database
    conn = connect_db()
    # create the cursor
    cursor = conn.cursor()

    # get
    cursor.execute('''
        SELECT eventId, eventName, eventType, date, startTime, endTime,
               targetAudience, description, roomId
        FROM event
        WHERE eventName LIKE ? OR date = ?
    ''', ('%' + search_term + '%', search_term))

    events = cursor.fetchall()
    conn.close()

    # in the case where there are no events
    if not events:
        print("\nNo events found")
        return

    print(f"\nFound {len(events)} events:")

    # print out the event in this format
    # testing it out

    # for event in events:
    # if detailed:
    #    print(f'''
    #    ID: {event['eventId']}
    #     Name: {event['eventName']}
    #    Type: {event['eventType']}
    #    Date: {event['date']}
    #    Time: {event['startTime']} - {event['endTime']}
    #    Audience: {event['targetAudience']}
    #    Description: {event['description']}
    #     Room: {event['roomId']}
    #    '''


connect_db()
find_event()
