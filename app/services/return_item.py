from setup_database import connect_db
import sqlite3
from datetime import datetime
# Return a borrowed item
# Optional can also just return the transactionID
def return_item(memberID, itemID):  
      # connect to the db
    conn = connect_db()
    
    # create cursor
    cursor = conn.cursor()
    
    try:
        # check if the transaction exists
        tCheckQuery = "SELECT * FROM borrow_transaction t WHERE t.itemID = ? AND t.memberID = ? AND t.returnDate IS NULL;"
        cursor.execute(tCheckQuery, (itemID, memberID,))
        tCheck = cursor.fetchone()
        if not tCheck:
            print("Sorry an active transaction does not exist for provided member and item.")
            return None
        # Get the current date, make it return date and update the borrowTransaction with same transactionID
        transactionID = tCheck["transactionID"]
        currentDate = datetime.now().strftime("%Y-%m-%d")
        updateDateQuery = "UPDATE borrow_transaction SET returnDate = ? WHERE transactionID = ?"
        cursor.execute(updateDateQuery, (currentDate, transactionID))
        # commit the changes
        conn.commit()
        dueDate = datetime.strptime(tCheck["dueDate"], "%Y-%m-%d")
        days_overdue = (datetime.now() - dueDate).days
        # Add a fine amount to charge if the due date is past
        fine_amount = days_overdue * 0.25
        # add the fine to the fine table in db and update transaction
        cursor.execute("SELECT MAX(fineID) AS fineID FROM fine;")
        maxFine = cursor.fetchone()["fineID"]
        fineID = maxFine + 1
        fineQuery = 'INSERT INTO fine (fineID, memberID, transactionID, amount, issueDate, paymentDate) VALUES (?,?,?,?,?,?)'
        cursor.execute(fineQuery, (fineID, memberID, transactionID, fine_amount, currentDate, None))
        conn.commit()
        updateBT = "UPDATE borrow_transaction SET fineAmount = ? WHERE transactionID = ?;"
        cursor.execute(updateBT, (fine_amount, transactionID))
        conn.commit()
        # Update the item table and available copies
        updateItemCopies = "UPDATE item SET availableCopies = availableCopies + 1 WHERE itemID = ?"
        cursor.execute(updateItemCopies, (itemID,))
        conn.commit()
        print("Sucessfully returned item.")
        if fine_amount > 0:
            print(f"Fine applied for late return: ${fine_amount:.2f}")

    except sqlite3.Error as e:
        print("Error returning item", e)
        
        
    conn.close()
    
    
    
   
# Testing only-------------------------------
# memberID = input("Enter memberID: ")
# itemID = input("Enter itemID: ")
# return_item(memberID, itemID)

 
   
