import sqlite3
from setup_database import connect_db

# Function to allow the user to sign in as library member
def login(email):
     # connect to the db
    conn = connect_db()
    
    # create cursor
    cursor = conn.cursor()
    
    try:
        # check if the user exists 
        userQuery = "SELECT * FROM member m WHERE m.email = ?;"
        cursor.execute(userQuery, (email,))
        member = cursor.fetchone()
        # return if member not found
        if not member:
            # print("Member not found. Please provide a different email.")
            return None
        firstName = member["firstName"]
        memberID = member["memberID"]
        print("Login success! Welcome,", firstName)
        return memberID
    except sqlite3.Error as e:
        print("Error logging in", e)
        
    # close the connection
    conn.close()
    
# Testing purposes only-------------------------
# login('michael.brown@email.com')