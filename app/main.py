import sqlite3
import questionary
from services.borrow_item import borrow_item
from services.donate_item import donate_item
from services.find_item import find_item_basic, find_item_keyword, findByItemID
from services.memberLogin import login
from services.return_item import return_item, show_borrowed_item
from services.librarian_help import request_librarian_assistance
from services.volunteer import volunteer_for_event
from services.find_event import find_event
from services.register_event import _register_for_event
from services.register_event import _view_event_registrations
import os


# global variable for the memberID of logged in user
LOGGED_IN_MEMBER_ID = None

# function to clear the screen each time. For better user experience


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def memLogin():
    global LOGGED_IN_MEMBER_ID
    while True:
        clear_screen()
        # ask for the user email
        print("--Aura Library Member Login--\n")
        memberEmail = questionary.text("Enter your email: ").ask()
        loginRes = login(memberEmail)
        if loginRes:
            LOGGED_IN_MEMBER_ID = loginRes
            return
            break
        else:
            print("Member not found.")
        input("\nPress Enter to try again...")

# menu to find an item


def memFindItem():
    while True:
        clear_screen()
        action = questionary.select(
            "Find Item - Choose an action:",
            choices=["Find By Title", "Find By Author",
                     "Find By ISBN", "Find By Keyword", "Back"]
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


def memBorrowItem():
    while True:
        global LOGGED_IN_MEMBER_ID
        clear_screen()
        action = questionary.select(
            "Borrow Item - Choose an action:",
            choices=["Borrow an Item", "Back"]
        ).ask()

        if action == "Borrow an Item":
            # ask for the title
            title = questionary.text("Enter the title: ").ask()
            titleRes = find_item_basic(title=title)
            if titleRes:
                # get the itemID
                itemID = titleRes[0]["itemID"]
                # send to borrowItem function
                borrow_item(itemID, memberID=LOGGED_IN_MEMBER_ID)
            else:
                print("Not found")
            input("\nPress Enter to return to the menu...")
        elif action == "Back":
            return


def memReturnItem():
    while True:
        global LOGGED_IN_MEMBER_ID
        clear_screen()
        action = questionary.select(
            "Return Item - Choose an action:",
            choices=["Return an Item", "Back"]
        ).ask()

        if action == "Return an Item":
            # show list of borrwed items
            borrowedList = show_borrowed_item(LOGGED_IN_MEMBER_ID)

            if borrowedList:
                # title, itemID list
                itemsList = []
                for item in borrowedList:
                    # get the itemID of each borrowed item
                    itemID = dict(item)["itemID"]
                    # get the item details of that item
                    res = findByItemID(itemID)
                    # get the item details
                    for row in res:
                        title = dict(row)["title"]
                        itemsList.append((title, itemID))

                # extract the titles and itemIDs for each borrowed item
                borrowOptions = [
                    f"{tup_title} (ID: {tup_itemID})" for tup_title, tup_itemID in itemsList]

                # ask the user to select the item
                selected_option = questionary.select(
                    "Which item would you like to return?",
                    choices=borrowOptions
                ).ask()

                # extract the item id form the list
                selected_itemID = int(selected_option.split(
                    " (ID: ")[1].replace(")", ""))

                print("Returning item...")
                # return item
                return_item(LOGGED_IN_MEMBER_ID, selected_itemID)
            else:
                print("You have no borrowed items")
            input("\nPress Enter to return to the menu...")

        elif action == "Back":
            return


def memDonateItem():
    while True:
        global LOGGED_IN_MEMBER_ID
        clear_screen()
        action = questionary.select(
            "Donate Item - Choose an action:",
            choices=["Donate an Item", "Back"]
        ).ask()

        if action == "Donate an Item":
            title = questionary.text("Enter the title: ").ask()
            author = questionary.text("Enter the author: ").ask()
            publisher = questionary.text("Enter the publisher: ").ask()
            year = questionary.text("Enter the publication year: ").ask()
            edition = questionary.text("Enter the edition: ").ask()
            genre = questionary.text("Enter the genre: ").ask()
            language = questionary.text("Enter the language: ").ask()
            isbn = questionary.text("Enter the ISBN: ").ask()
            totalCopies = questionary.text("Enter number of copies: ").ask()
            # Send the attributes to donate item function
            donate_item(title, author, publisher, year, edition,
                        genre, language, isbn, totalCopies)
            input("\nPress Enter to return to the menu...")
        elif action == "Back":
            return

def memFindEvent():
    while True:
        clear_screen()
        action = questionary.select(
            "Find Event - Choose an action:",
            choices=[
                "Search Events",
                "View All Upcoming Events",
                "Back"
            ]
        ).ask()

        if action == "Search Events":
            search_term = questionary.text("Search by event name or date (YYYY-MM-DD):").ask()
            find_event(search_term)  
            input("\nPress Enter to return to the menu...")
            
        elif action == "View All Upcoming Events":
            find_event()  # Call without arguments to show all
            input("\nPress Enter to return to the menu...")
            
        elif action == "Back":
            return

def memRequestHelp():
    while True:
        global LOGGED_IN_MEMBER_ID
        clear_screen()
        action = questionary.select(
            "Ask a Librarian For Help - Choose an action:",
            choices=["Ask a Librarian For Help", "Back"]
        ).ask()

        if action == "Ask a Librarian For Help":
            request_librarian_assistance(LOGGED_IN_MEMBER_ID)
            print("\nYour request for librarian assistance has been sent successfully!")
            input("\nPress Enter to return to the menu...")
        elif action == "Back":
            return  # Exit the function and go back to the main menu

def memRegisterEvent():
    while True:
        global LOGGED_IN_MEMBER_ID
        clear_screen()
        action = questionary.select(
            "Event Registration - Choose an action:",
            choices=[
                "Register for Event",
                "View My Event Registrations",
                "Back"
            ]
        ).ask()

        if action == "Register for Event":
            if LOGGED_IN_MEMBER_ID is None:
                print("Please login first.")
                input("\nPress Enter to continue...")
                continue
                
            _register_for_event(LOGGED_IN_MEMBER_ID)
            input("\nPress Enter to return to the menu...")
            
        elif action == "View My Event Registrations":
            if LOGGED_IN_MEMBER_ID is None:
                print("Please login first.")
                input("\nPress Enter to continue...")
                continue
                
            _view_event_registrations(LOGGED_IN_MEMBER_ID)
            input("\nPress Enter to return to the menu...")
            
        elif action == "Back":
            return

def memVolunteer():
    while True:
        global LOGGED_IN_MEMBER_ID
        clear_screen()
        action = questionary.select(
            "Volunteer for Library - Choose an action:",
            choices=["Volunteer for Event", "Back"]
        ).ask()

        if action == "Volunteer for Event":
            if LOGGED_IN_MEMBER_ID is None:
                print("Please login first.")
                input("\nPress Enter to continue...")
                continue
                
            volunteer_for_event(loginID=LOGGED_IN_MEMBER_ID)  # Changed LOGIN_ID to loginID
            
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
                "Ask a Librarian for Help",
                "Logout",
                "Exit"
            ]
        ).ask()
        if choice == "Find Item":
            memFindItem()
        elif choice == "Borrow Item":
            memBorrowItem()
        elif choice == "Return Item":
            memReturnItem()
        elif choice == "Donate Item":
            memDonateItem()
        elif choice == "Find Event":
            memFindEvent()
        elif choice == "Register for Event":
            memRegisterEvent()
        elif choice == "Volunteer for Library":
            memVolunteer()
        elif choice == "Ask a Librarian for Help":
            memRequestHelp()
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
