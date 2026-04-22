contacts = []

while True:
    print("\n1. Add Contact")
    print("2. Remove Contact")
    print("3. View Contacts")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter contact Name: ")
        contacts.append(name)
        print("Contact added!")

    elif choice == "2":
        name = input("Enter contact to remove: ")
        if name in contacts:
            contacts.remove(name)
            print("Contact removed!")
        else:
            print("Contact not found.")

    elif choice == "3":
        print("Contacts: ", contacts)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
