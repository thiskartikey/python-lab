phone_book = {}

def add_contact():
    person_name = input("Enter name: ").strip()
    contact_number = input("Enter phone number: ").strip()
    phone_book[person_name] = contact_number
    print("Contact added successfully.")

def view_contacts():
    if not phone_book:
        print("No contacts available.")
        return
    print("\nContacts:")
    for person_name, contact_number in phone_book.items():
        print(person_name, ":", contact_number)

def search_contact():
    query_name = input("Enter name to search: ").strip()
    if query_name in phone_book:
        print("Phone number:", phone_book[query_name])
    else:
        print("Contact not found.")

def update_contact():
    target_name = input("Enter name to update: ").strip()
    if target_name in phone_book:
        new_number = input("Enter new phone number: ").strip()
        phone_book[target_name] = new_number
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    remove_name = input("Enter name to delete: ").strip()
    if remove_name in phone_book:
        del phone_book[remove_name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Directory ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        selection = input("Enter your choice: ").strip()
        if selection == "1":
            add_contact()
        elif selection == "2":
            view_contacts()
        elif selection == "3":
            search_contact()
        elif selection == "4":
            update_contact()
        elif selection == "5":
            delete_contact()
        elif selection == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
