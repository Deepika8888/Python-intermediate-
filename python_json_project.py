#lets work on a small project 
#lets create a contact book using json 

import json
import os

#lets ask for their name and phone number

name = input("Please enter your name: ")
phone = int(input("please enter your phone number: "))

new_contact = {
    "name": name, 
    "Phone Number": phone

}

contacts = []

if os.path.exists("contacts.json"):
    with open ("contacts.json", 'r') as file:
        try:
            contacts = json.load(file)
        except  json.JSONDecodeError:
            print("⚠️ Empty or corrupted file, starting fresh.")


#adding a new contact 

contacts.append(new_contact)

#saving all the contacts back to the file 

with open("contacts.json", 'w') as file: 
    json.dump(contacts, file, indent=4)

#showing all the contacts 

print("\n All Saved Contacts:")
for i, contact in enumerate(contacts, start=1):
    print(f"{i}. {contact['name']} - {contact['Phone Number']}")




