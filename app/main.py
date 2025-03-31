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

def memFindItem():
    clear_screen()
    action = questionary.select(
        "Find Item - Choose an action:",
        choices=["Find By Title", "Find By Author", "Find By ISBN", "Find By Keyword", "Back"]
    ).ask()

    if action == "Find By Title":
        print("Auraaaa")
    elif action == "Find By Author":
        print("Auraaaa")
    elif action == "Find By ISBN":
        print("Auraaaa")
    elif action == "Find By Keyword":
        print("Auraaaa MAxingggg")
    elif action == "Back":
        return
        


def main_menu():
    while True:
        global LOGGED_IN_MEMBER_ID
        clear_screen()
        if LOGGED_IN_MEMBER_ID is None:
            memLogin()  # Ensure user is logged in before showing the menu
        choice = questionary.select(
            "\n\nAura Library Management System - Choose an option:",
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