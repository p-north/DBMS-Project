from setup_database import connect_db
import sqlite3


# Basic-Search
# Keyword-Based

def find_item_basic(title=None, author=None, ISBN=None):
    
    
    
    # User input title, author or ISBN
    conn = connect_db()
    
    # Create a cursor
    cursor = conn.cursor()
    
    # sql query
    query = None
    result = None

    
    if title:
        query = "SELECT * FROM item i WHERE i.title LIKE '%' || ?;"
        # execute the query in try catch block
        try:
            cursor.execute(query,(title.title(),))
            result = cursor.fetchall()  # Add to the result list)
        except sqlite3.Error as e:
            print("Error fetching title for item...", e)
    if author:
        query = "SELECT * FROM item i WHERE i.author LIKE '%' || ? ?"
        # execute the query in try catch block
        try:
            cursor.execute(query,(author.title(),))
            result = cursor.fetchall()  # Add to the result list
        except sqlite3.Error as e:
            print("Error fetching author for item...",e)
    if ISBN:
        query = "SELECT * FROM item i WHERE i.ISBN = ?"
        # execute the query in try catch block
        try:
            cursor.execute(query,(ISBN,))
            result = cursor.fetchall()  # Add to the result list
        except sqlite3.Error as e:
            print("Error fetching ISBN for item...", e)
    

    
        
    # close connnection
    conn.close()
    return result


# Optional-------------------------------  
# def find_item_advanced(keyword):
    
#     # User input title, author or ISBN
#     conn = connect_db()
    
#     # Create a cursor
#     cursor = conn.cursor()
    
#     # sql query
#     # query = 
 
    
def find_item_keyword(keyword):
    
    # User input title, author or ISBN
    conn = connect_db()
    
    # Create a cursor
    cursor = conn.cursor()
    
    # sql query
    query = "SELECT * FROM item WHERE title LIKE '%' || ? || '%' OR author LIKE '%' || ? || '%' OR ISBN LIKE '%' || ? || '%'"
    result = None
    try:
        cursor.execute(query, (keyword, keyword, keyword))
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print('Error fetching by keyword', e)
        
    cursor.close()
    return result

# Helper function find an item by the item id
def findByItemID(itemID):
    # User input title, author or ISBN
    conn = connect_db()
    
    # Create a cursor
    cursor = conn.cursor()
    
    iQuery = "SELECT * FROM item i WHERE i.itemID = ?"
    cursor.execute(iQuery, (itemID,))
    res = cursor.fetchall()
    return res
    

# # Testing Purposes Only ---------------------------------
# title = input("Enter title ")
# res = find_item_basic(title)
# if res:
#     for row in res:
#         print(dict(row))
# else:
#     print("Not found")

# Testing Purposes Only ---------------------------------
# keyword = input("Enter keyword: ")
# res = find_item_keyword(keyword)
# if res:
#     for row in res:
#         print(dict(row))
# else:
#     print("Not found")

    