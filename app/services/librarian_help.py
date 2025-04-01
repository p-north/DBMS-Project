import sqlite3
from setup_database import connect_db



def request_librarian_assistance(loginID):
    print("\nLibrary Help Request System")
    print("--------------------------")

    try:
        conn = connect_db()
        cursor = conn.cursor()

        member_id = loginID

        # Display request topics
        topics = [
            "Research Assistance", "Finding a Book", "Citation Help",
            "Library Card Issues", "E-Book Access", "Historical Archives",
            "Interlibrary Loan", "Tech Help", "Audiobook Recommendations", "Library Tour"
        ]

        print("\nAvailable Request Topics:")
        for i, topic in enumerate(topics, 1):
            print(f"{i}. {topic}")

        topic_choice = input("\nEnter request topic (1-10): ")
        try:
            topic_choice = int(topic_choice)
            if 1 <= topic_choice <= 10:
                topic = topics[topic_choice - 1]
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Defaulting to 'Other'.")
            topic = "Other"

        # Set initial status
        status = "Pending"

        # Get available employees
        cursor.execute(
            "SELECT employeeID FROM personnel ORDER BY RANDOM() LIMIT 1")
        assigned_employee = cursor.fetchone()

        if assigned_employee:
            employee_id = assigned_employee[0]
        else:
            print("No employees available. Try again later.")
            return

        # Insert new help request
        cursor.execute(
            """
            INSERT INTO help_request (memberID, employeeID, requestDate, topic, status)
            VALUES (?, ?, DATE('now'), ?, ?)
            """,
            (member_id, employee_id, topic, status)
        )
        conn.commit()
        print("\nYour request has been submitted successfully!")
        print(f"Request ID: {cursor.lastrowid}")
        print(f"Topic: {topic}")
        print(f"Status: {status}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()


# Example usage
# request_librarian_assistance()
