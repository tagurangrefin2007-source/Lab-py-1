import os
users = []

while True:
    os.system("cls")
    print("1 - [ View users ]")
    print("2 - [ Add a user ]")
    print("3 - [ Delete a user ]")
    print("4 - [ Update a user ]")
    print("5 - [ Exit ]")
    
    usr_cmd = input("Input a command (1/2/3/4/5): ")

    if usr_cmd == "1":
        print("[--  Users  --]")
        for user in users:
            print(user)
            flow = input("Enter to go back... ")
    elif usr_cmd == "2":
        username = input("Enter a Username: ")
        users.append(username)
    elif usr_cmd == "3":
        username_delete = input("Enter a username to delete: ")
        if username_delete in users:
            users.remove(username_delete)
    elif usr_cmd == "4":
        username_update = input("Enter a username to update: ")
        new_username = input("Enter the new username: ")
        if username_update in users:
            index = users.index(username_update)
            users[index] = new_username
    elif usr_cmd == "5":
        print("Program ends ;)")
        break
    else:
        print("Invalid command")