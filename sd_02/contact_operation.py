import json


def load_contacts(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts(contacts, filename):
    with open(filename, 'w') as f:
        json.dump(contacts, f)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def edit_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the index of the contact to edit: ")) - 1
        contact = contacts[index]
        print("Editing contact:")
        print(f"1. Name: {contact['name']}")
        print(f"2. Phone: {contact['phone']}")
        print(f"3. Email: {contact['email']}")
        choice = int(input("Enter the number of the field to edit: "))
        if choice == 1:
            contact['name'] = input("Enter new name: ")
        elif choice == 2:
            contact['phone'] = input("Enter new phone number: ")
        elif choice == 3:
            contact['email'] = input("Enter new email address: ")
        else:
            print("Invalid choice.")
        print("Contact edited successfully.")
    except (IndexError, ValueError):
        print("Invalid index.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the index of the contact to delete: ")) - 1
        del contacts[index]
        print("Contact deleted successfully.")
    except (IndexError, ValueError):
        print("Invalid index.")


def main():
    contacts = load_contacts("contacts.json")
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts, "contacts.json")
            print("Exiting program. Contacts saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
