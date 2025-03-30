from ..setup_database import connect_db
import sqlite3
from datetime import datetime, timedelta


# Borrow an item from the library
def borrow_item(itemID, memberID):
    # connect to the db
    conn = connect_db()
    
    # create cursor
    cursor = conn.cursor()
    
    try:
        # Get the item that the user needs.
        getItemQuery = "SELECT * FROM item i WHERE i.itemID = ?;"
        cursor.execute(getItemQuery, (itemID,))
        # fetch the only item with itemID
        item = cursor.fetchone()
        # Make sure there's enough copies and its not checked out already
        availableCopies = item["availableCopies"]
        totalCopies = item["totalCopies"]
        if(availableCopies < 1):
            return None
        # If available, checkout the item
        # first reduce avalable copies from item
        reduceQuery = "UPDATE item SET availableCopies = availableCopies - 1 WHERE itemID = ?;"
        cursor.execute(reduceQuery, (itemID,))
        conn.commit()
        # checkout from borrow_transaction table
        cursor.execute("SELECT MAX(transactionID) AS transactionID FROM borrow_transaction")
        maxID = cursor.fetchone()
        # get ID for transaction
        transactionID = (maxID["transactionID"]) + 1
        # get the current date
        borrowDate = datetime.now().strftime("%Y-%m-%d")
        # add dueDate of +2 weeks
        dueDate =(datetime.now() + timedelta(weeks=2)).strftime("%Y-%m-%d")
        # 0.00 for now
        fineAmount = 0.00
        # Insertion query
        borrowQuery = "INSERT INTO borrow_transaction (transactionID, memberID, itemID, borrowDate, dueDate, returnDate, fineAmount) VALUES (?,?,?,?,?,?,?);"
        cursor.execute(borrowQuery, (transactionID, memberID, itemID, borrowDate, dueDate, None, fineAmount))
        # commit the borrow
        conn.commit()
        print("Borrow for item success")

    except sqlite3.Error as e:
        print("Error fetching item for borrow: ", e)
        
    # close connection
    conn.close()

# Testing only-------------------------------
# memberID = input("Enter memberID: ")
# itemID = input("Enter itemID: ")
# borrow_item(itemID, memberID)

    
    

