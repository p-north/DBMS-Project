import sqlite3
import questionary
from services.borrow_item import borrow_item
from services.donate_item import donate_item
from services.find_item import find_item_basic, find_item_keyword
from services.memberLogin import login
from services.return_item import return_item


# global variable for the memberID of logged in user
LOGGED_IN_MEMBER_ID = None

def memLogin():
    global LOGGED_IN_MEMBER_ID
    while True:
        # ask for the user email
        memberEmail = questionary.text("Enter your member email: ").ask()
        loginRes = login(memberEmail)
        if loginRes:
            LOGGED_IN_MEMBER_ID = loginRes 
            main_menu()
            break
        else:
            print("Member not found. Please try again.")


def main_menu():
    while True:
        choice = questionary.select(
            "\n\nAura Library Management System - Choose an option:",
            choices=[
                "Manage Members",
                "Manage Items",
                "Manage Transactions",
                "Exit"
            ]
        ).ask()
        if choice == "Exit":
            print("Goodbye!")
            break

if __name__ == "__main__":
    memLogin()