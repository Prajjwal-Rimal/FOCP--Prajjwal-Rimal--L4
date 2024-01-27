PASSWORD_FILE = "passwd.txt"


def read_users():
    with open(PASSWORD_FILE, "r") as file:
        lines = file.readlines()
    return [line.strip().split(":") for line in lines]


def write_users(users):
    with open(PASSWORD_FILE, "w") as file:
        for user in users:
            file.write(":".join(user) + "\n")


def adduser():
    users = read_users()

    username = input("Enter new username: ").strip()
    real_name = input("Enter real name: ").strip()
    password = input("Enter password: ").strip()

    if any(user[0] == username for user in users):
        print("Cannot add. Most likely username already exists.")
    else:
        users.append([username, real_name, password])
        write_users(users)
        print("User Created.")


def deluser():
    users = read_users()

    username = input("Enter username: ").strip()

    if any(user[0] == username for user in users):
        users = [user for user in users if user[0] != username]
        write_users(users)
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")


def passwd():
    users = read_users()

    username = input("User: ").strip()

    user_index = next((i for i, user in enumerate(users) if user[0] == username), None)

    if user_index is not None:
        current_password = input("Current Password: ").strip()
        new_password = input("New Password: ").strip()
        confirm_password = input("Confirm: ").strip()

        if users[user_index][2] == current_password and new_password == confirm_password:
            users[user_index][2] = new_password
            write_users(users)
            print("Password changed.")
        else:
            print("Invalid current password or passwords do not match. No change made.")
    else:
        print("User not found. No change made.")


def login():
    users = read_users()

    username = input("User: ").strip()
    password = input("Password: ").strip()

    if any(user[0] == username and user[2] == password for user in users):
        print("Access granted.")
    else:
        print("Access denied.")


login()
adduser()
deluser()
passwd()

