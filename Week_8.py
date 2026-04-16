
try:
    file = open("message.txt", "x")
    print("File created successfully!")
    file.close()
except FileExistsError:
    print("Error: File already exists.")


while True:
    try:
        print("\nMENU")
        print("1 - Send a message")
        print("2 - View messages")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            message = input("Enter your message: ")
            with open("message.txt", "a") as file:
                file.write(message + "\n")
            print("Message saved!")

        elif choice == "2":
            with open("message.txt", "r") as file:
                content = file.read()
                print("\nMessages:")
                print(content)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

    except Exception as e:
        print("Error occurred:", e)