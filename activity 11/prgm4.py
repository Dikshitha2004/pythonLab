contacts = {
    "Alice": "1234567890",
    "Bob": "9876543210"
}

name = input("Enter contact name: ")
phone = input("Enter phone number: ")

if name in contacts:
    contacts[name] = phone
    print(f"Updated contact for {name}.")
else:
    contacts[name] = phone
    print(f"Added new contact for {name}.")

print("Contact Book:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")
