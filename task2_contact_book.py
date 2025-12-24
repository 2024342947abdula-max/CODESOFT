import json
import os

CONTACT_FILE = "contacts.json"

# Load contacts from file (if exists)
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact():
    print("\n--- ADD NEW CONTACT ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    if not name or not phone:
        print("ERROR: Name and Phone number are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    print("\n--- CONTACT LIST ---")
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

# Search contact by name or phone
def search_contact():
    print("\n--- SEARCH CONTACT ---")
    keyword = input("Enter Name or Phone Number to search: ").strip()
    contacts = load_contacts()
    results = [c for c in contacts if keyword.lower() in c['name'].lower() or keyword in c['phone']]

    if results:
        for c in results:
            print(f"\nName: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
    else:
        print("No matching contacts found.")

# Update existing contact
def update_contact():
    print("\n--- UPDATE CONTACT ---")
    name = input("Enter the name of the contact to update: ").strip()
    contacts = load_contacts()

    for c in contacts:
        if c['name'].lower() == name.lower():
            print(f"Current Details: {c}")
            c['phone'] = input(f"New Phone ({c['phone']}): ").strip() or c['phone']
            c['email'] = input(f"New Email ({c['email']}): ").strip() or c['email']
            c['address'] = input(f"New Address ({c['address']}): ").strip() or c['address']
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact():
    print("\n--- DELETE CONTACT ---")
    name = input("Enter the name of the contact to delete: ").strip()
    contacts = load_contacts()

    updated_contacts = [c for c in contacts if c['name'].lower() != name.lower()]

    if len(updated_contacts) == len(contacts):
        print("No contact found with that name.")
    else:
        save_contacts(updated_contacts)
        print("Contact deleted successfully!")

# Main Menu
def main():
    while True:
        print("""
=== CONTACT BOOK ===
1. Add Contact
2. View Contact List
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
""")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
