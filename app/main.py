import sqlite3
import questionary
from services.borrow_item import borrow_item
from services.donate_item import donate_item
from services.find_item import find_item_basic, find_item_keyword
from services.memberLogin import login
from services.return_item import return_item
import os


# global variable for the memberID of logged in user
LOGGED_IN_MEMBER_ID = None

# function to clear the screen each time. For better user
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def memLogin():
    global LOGGED_IN_MEMBER_ID
    while True:
        clear_screen()
        # ask for the user email
        memberEmail = questionary.text("Enter your member email: ").ask()
        loginRes = login(memberEmail)
        if loginRes:
            LOGGED_IN_MEMBER_ID = loginRes 
            return
            break
        else:
            print("Member not found. Please try again.")

# menu to find an item
def memFindItem():
    while True:
        clear_screen()
        action = questionary.select(
            "Find Item - Choose an action:",
            choices=["Find By Title", "Find By Author", "Find By ISBN", "Find By Keyword", "Back"]
        ).ask()

        if action == "Find By Title":
            title = questionary.text("Enter the title: ").ask()
            res = find_item_basic(title=title)
            if res:
                print("\nSearch Results:")
                for row in res:
                    print("Title: ", dict(row)["title"])
                    print("Type: ", dict(row)["itemType"])
                    print("Author: ", dict(row)["author"])
                    print("Publisher: ", dict(row)["publisher"])
                    print("Year: ", dict(row)["publicationYear"])
                    print("Edition: ", dict(row)["edition"])
                    print("Genre: ", dict(row)["genre"])
                    print("Language: ", dict(row)["language"])
                    print("Copies Available: ", dict(row)["availableCopies"])
                    print("Copies Total: ", dict(row)["totalCopies"])
                    print("Location: ", dict(row)["location"])
                    
            else:
                print("Not found")
            input("\nPress Enter to return to the menu...")
        elif action == "Find By Author":
            author = questionary.text("Enter the author: ").ask()
            res = find_item_basic(author=author)
            if res:
                print("\nSearch Results:")
                for row in res:
                    print("Title: ", dict(row)["title"])
                    print("Type: ", dict(row)["itemType"])
                    print("Author: ", dict(row)["author"])
                    print("Publisher: ", dict(row)["publisher"])
                    print("Year: ", dict(row)["publicationYear"])
                    print("Edition: ", dict(row)["edition"])
                    print("Genre: ", dict(row)["genre"])
                    print("Language:  ", dict(row)["language"])
                    print("Copies Available: ", dict(row)["availableCopies"])
                    print("Copies Total: ", dict(row)["totalCopies"])
                    print("Location: ", dict(row)["location"])
                    
            else:
                print("Not found")
            input("\nPress Enter to return to the menu...")
        elif action == "Find By ISBN":
            ISBN = questionary.text("Enter the ISBN: ").ask()
            res = find_item_basic(ISBN=ISBN)
            if res:
                print("\nSearch Results:")
                for row in res:
                    print("Title: ", dict(row)["title"])
                    print("Type: ", dict(row)["itemType"])
                    print("Author: ", dict(row)["author"])
                    print("Publisher: ", dict(row)["publisher"])
                    print("Year: ", dict(row)["publicationYear"])
                    print("Edition: ", dict(row)["edition"])
                    print("Genre: ", dict(row)["genre"])
                    print("Language:  ", dict(row)["language"])
                    print("Copies Available: ", dict(row)["availableCopies"])
                    print("Copies Total: ", dict(row)["totalCopies"])
                    print("Location: ", dict(row)["location"])
                    
            else:
                print("Not found")
            input("\nPress Enter to return to the menu...")
        elif action == "Find By Keyword":
            keyword = questionary.text("Enter a keyword: ").ask()
            res = find_item_keyword(keyword)
            if res:
                print("\nSearch Results:")
                for row in res:
                    print("Title: ", dict(row)["title"])
                    print("Type: ", dict(row)["itemType"])
                    print("Author: ", dict(row)["author"])
                    print("Publisher: ", dict(row)["publisher"])
                    print("Year: ", dict(row)["publicationYear"])
                    print("Edition: ", dict(row)["edition"])
                    print("Genre: ", dict(row)["genre"])
                    print("Language:  ", dict(row)["language"])
                    print("Copies Available: ", dict(row)["availableCopies"])
                    print("Copies Total: ", dict(row)["totalCopies"])
                    print("Location: ", dict(row)["location"])
                    print("\n-------------------------------------------------\n")
                    
            else:
                print("Not found")
            input("\nPress Enter to return to the menu...")    
        elif action == "Back":
            return
            
# test email: john.smith@email.com

def main_menu():
    while True:
        global LOGGED_IN_MEMBER_ID
        clear_screen()
        if LOGGED_IN_MEMBER_ID is None:
            memLogin()  # Ensure user is logged in before showing the menu
        choice = questionary.select(
            f"\n\nMemberId: {LOGGED_IN_MEMBER_ID}\n Aura Library Management System - Choose an option:",
            choices=[
                "Find Item",
                "Borrow Item",
                "Return Item",
                "Donate Item",
                "Find Event",
                "Register for Event",
                "Volunteer for Library",
                "Ask a Librarian for Help ",
                "Logout",
                "Exit"
            ]
        ).ask()
        if choice == "Find Item":
            memFindItem()
            
        elif choice == "Logout":
            print("Logging out...")
            LOGGED_IN_MEMBER_ID = None
            memLogin()
        elif choice == "Exit":
            print("Goodbye!")
            LOGGED_IN_MEMBER_ID = None
            break

if __name__ == "__main__":
    main_menu()