"""
This file is a textual UI layer on top of the phone app.
It will allow a user to view, add, and delete contacts,
as well as make calls and send texts.
"""

from phone import Phone

def display_menu():
    print '''
        0 - Main Menu
        1 - Show all contacts
        2 - Add a new contact
        3 - Delete a contact
        4 - Make a phone call
        5 - Send a text
        6 - Exit the program
    '''

def display_contacts(phone):

    contacts = phone.contacts.values()
    if contacts:
        for contact in contacts:
            print contact.full_name(), contact.phone_number
    else:
        print "No contacts found"


def main():

    phone_name = raw_input("Enter the name of your phone: ")
    number = int(raw_input("Enter your number: "))
    phone = Phone(number, phone_name)
    print "Congratulations! You've set up your phone!"
    while True:
        display_menu()
        choice = raw_input("Please select an action: ")
        if choice == "0":
            display_menu()
        elif choice == "1":
            display_contacts(phone)
        elif choice == "2":
            first_name = raw_input("Enter the contact's first name: ")
            last_name = raw_input("Enter the contact's last name: ")
            number = int(raw_input("Enter the contact's number: "))
            phone.add_contact(first_name, last_name, number)
            print "Congrats you added a contact"
        elif choice == "3":
            first_name = raw_input("Enter the contact's first name: ")
            last_name = raw_input("Enter the contact's last name: ")
            phone.del_contact(first_name, last_name)
            print "You've deleted", first_name + last_name
        elif choice == "4":
            first_name = raw_input("Enter the contact's first name: ")
            last_name = raw_input("Enter the contact's last name: ")
            phone.call(first_name, last_name)
        elif choice == "5":
            first_name = raw_input("Enter the contact's first name: ")
            last_name = raw_input("Enter the contact's last name: ")
            message = raw_input("Enter the text message: ")
            print "USE AN METHOD FROM THE PHONE CLASS TO SEND TEXT"
        elif choice == "6":
            break
        else:
            print "Invalid selection. Please choose again."


if __name__ == '__main__':
    main()
