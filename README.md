# 🐍 Mini Project Module 3

Welcome to the Contact Management System! This application
allows you to manage your contacts efficiently. You can add,
edit, delete, search, view, export, and import contacts with ease.

## 📂 Getting Started

Follow these steps to use the Contact Management System:

Prerequisites:
> Python 3.6 or higher installed on your computer.

Running the Program:
> - Save the provided code in a file named `ContactManagementSystem.py`
> - Open a terminal or command prompt
> - Navigate to the directory containing `ContactManagementSystem.py`
> - Run the program using the command:
```
python ContactManagementSystem.py
```

## Features 
1. Add a New Contact
    - Enter the contact's full name, phone number, and email address.
    - The program validates the phone number and email address before adding the contact.

2. Edit an Existing Contact
    - View a list of all contacts
    - Select the contact your want to edit by its number
    - UPdate the name, phone number, and email address

3. Delete a Contact
    - View a list of all contacts
    - Select the contact you want to delete by its number

4. Search for a Contact
    - Enter the first name of the contact your want to find
    - The program searches for matching contacts and displays the results

5. Display all Contacts
    - View all saved contacts in a numbered list

6. Export Contacts
    - Export all saved contacts to a text file named `contacts.txt` in JSON format.

7. Import Contacts
    - Import contacts from an existing `contacts.txt` file
    - Merged data will include all previosuly saved and newly imported contacts

8. Quit
    - Exit the program

## Notes
>   - The phone number must match `1-XXX-XXXX` format
>   - The email address must follow a valid format, e.g., `example@domain.com`
>   - If any input is invalid, the program will prompt you to try again

## Error Handling
>   - KeyError: Occurs when trying to access a contact that doesn't exist
>   - ValueError: Occurs when entering invalid inputs. The program will prompt you to try again. 

## File Management
>   - `contacts.txt` is used to save and retrieve contacts
>   - Ensure `contacts.txt` is in the same directory as the program for importing contacts

## Example Usage

### Adding a Contact
```
Enter contact full name: Christopher Tucker
Enter contact phone number: 1-123-456-7890
Approved Number
Enter contact email: TuckerTimes@example.com
Approved Email
Your contact Christopher Tucker has been added!
```

## Viewing All Contacts
```
Contact Number #1 - Contact Info: {'Name': 'John Doe', 'Phone Number': '1-800-000-0000', 'Email': 'JohnDoe@gmail.com'}
Contact Number #2 - Contact Info: {'Name': 'Jane Doe', 'Phone Number': '1-989-111-9111', 'Email': 'JaneDoe@outlook.com'}
```

## License

*This Contact Management System is open-source. Feel free to modify and use it as needed.*