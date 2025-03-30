from ..setup_database import connect_db
import sqlite3
import random
import string

# Donate an item/book to the library
def donate_item(title, author, publisher, publicationYear, edition, genre, language, ISBN, totalCopies):
     # connect to the db
    conn = connect_db()
    
    # create cursor
    cursor = conn.cursor()
    # Default item type
    itemType = 'Book'
    # create random location
    location = 'Shelf ' + str(random.choice(string.ascii_uppercase)) + str(random.choice(string.digits))
    print(location)
    

    try:
        dupCheckQuery = "SELECT * FROM item i WHERE i.ISBN = ?"
        cursor.execute(dupCheckQuery, (ISBN,))
        dupCheck = cursor.fetchone()
        # If the book already exists in db with same ISBN only update the availableCopies and totalCopies
        if dupCheck:
            updateISBN = "UPDATE item SET availableCopies = availableCopies + ?, totalCopies = totalCopies + ? WHERE item.ISBN = ?"
            cursor.execute(updateISBN, (totalCopies, totalCopies, ISBN)) 
            # commit the update
            conn.commit()
            
            
        # else insert as new item
        else:
            cursor.execute("SELECT MAX(itemID) as itemID FROM item;")
            itemID = cursor.fetchone()["itemID"] + 1
            newItem = "INSERT INTO item (itemID, title, itemType, author, publisher, publicationYear, edition, genre, language, ISBN, availableCopies, totalCopies, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);"
            cursor.execute(newItem, (itemID, title, itemType, author, publisher, publicationYear, edition, genre, language, ISBN, totalCopies, totalCopies, location))
            # commit the insertion
            conn.commit()
    except sqlite3.Error as e:
        print("Error donating item ", e)
        
    print("Item sucesssfully added. Thank you for donating!")    
    conn.close()



# Testing purposes only----------------------------------
# donate_item(
#     title="The Art of Code",
#     author="John Doe",
#     publisher="TechPress",
#     publicationYear=2021,
#     edition=2,
#     genre="Technology",
#     language="English",
#     ISBN="978-3-16-148410-0",
#     totalCopies=5
# )
    
    

