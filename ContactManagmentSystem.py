import re
import json

def ContactManagementSystem():
    contacts = {
        1 : {
        "Name" : "John Doe",
        "Phone Number": "1-800-000-0000",
        "Email": "JohnDoe@gmail.com"
        },
        2 : {
        "Name" : "Jane Doe",
        "Phone Number": "1-989-111-9111",
        "Email": "JaneDoe@outlook.com"
        }
    }

    def new_contact(contacts):
        name = input("Enter contact full name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        update = (len(contacts.keys()) + 1)
        contacts[update] = {
            "Name": name,
            "Phone Number": phone,
            "Email": email
        }
        print(f"You contact {name} has been added!")
    
    def edit_contact(contacts):
        for x, y in contacts.items():
            print(f"{x} - {y}")
        editer = input("Please select the contact you would like to edit: ")
        name = input("Enter contact full name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contacts[int(editer)].update({
            "Name": name,
            "Phone Number": phone,
            "Email": email
        })
        print(f"Your contact {name} has been updated!")
    
    def delete_contact(contacts):
        for x, y in contacts.items():
            print(x, y)
        editer = input("Please select the contact you would like to delete: ")
        del contacts[int(editer)]
        print(f"Your contact {editer} has been deleted")
        for x, y in contacts.items():
            print(f"{x} - {y}")
    
    def search_contact(contacts):
        search = (input("Please enter the first name of the contact you would like to find: ")).lower()
        for contact in contacts.values():
            x = re.search(f"^{search}", contact["Name"].lower())
            if x:
                print(f"Found {search} in your contacts!")
        if not x: 
            print("Not Found!")

    def view_all(contacts):
        for x, y in contacts.items():
            print(f"Contact Number #{x} - Contact Info: {y}")

    def export_contact(contacts):
        with open('contacts.txt', 'w') as export_file:
            export_file.write(json.dumps(contacts))
        confirm = open('contacts.txt', 'r')
        print(confirm.read())

    def import_contact():
        data = {}
        with open('contacts.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split(':', 1)
                data[key] = value
        print(data)
        
    while True:
        try:
            print("\nWelcome to the Contact Management System")
            print("\nMenu \n1. Add a new contact \n2. Edit an existing contact \n3. Delete a contact \n4. Search for a contact \n5. Display all contacts \n6. Export contacts to a text file \n7. Import contact from a text file \n8. Quit")
            option = input("\nPlease choose your option: ")
            if option == "1":
                new_contact(contacts)
            elif option == "2":
                edit_contact(contacts)
            elif option == "3":
                delete_contact(contacts)
            elif option == "4":
                search_contact(contacts)
            elif option == "5":
                view_all(contacts)
            elif option == "6":
                export_contact(contacts)
            elif option == "7":
                import_contact()
            elif option == "8":
                print("Goodbye, have a nice day!")
                break

        except KeyError: 
            print("Please, try again.")
        except ValueError:
            print("Please, try again.")

ContactManagementSystem()