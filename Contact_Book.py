import os

#---------------------------------------------Contact Class---------------------------------#
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
    
#---------------------------------------------ContactBook Class---------------------------------#
class ContactBook:
    def __init__(self, filename='contacts.txt'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name, phone, email = line.strip().split(' || ')
                    contacts.append(Contact(name, phone, email))
        return contacts

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name}|{contact.phone}|{contact.email}\n")

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def delete_contact(self, name):
        initial_count = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        if len(self.contacts) == initial_count:
            print("Contact not present.")
        else:
            self.save_contacts()
            print("Contact deleted.")

#---------------------------------------------Main Function---------------------------------#
def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)
            print("Contact added.")

        elif choice == '2':
            print("Contacts:")
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
