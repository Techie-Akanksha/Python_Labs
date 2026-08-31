import random
import string
#EXPENSE TRACKER

print("="*75)
print("                         PASSWORD MANAGER                         ")
print("="*75)
print()

accounts = []

def add_acc():
    print("Adding account...")
    website = input("Enter your website: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    account = {
        "website": website,
        "username": username,
        "password": password
    }
    accounts.append(account)
    print("Account added successfully!")
    print()

def view_acc():
    print("Showing account...")
    if len(accounts) == 0:
        print("No accounts found")
        print()
        return

    # The enumerate() function in Python is a built-in tool that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object. It is primarily used in loops to track both the index and the value of items simultaneously without managing a manual counter variable
    for i, account in enumerate(accounts, start=1):
        print("Account", i)
        print("Website:", account["website"])
        print("Username:", account["username"])
        print("Password:", account["password"])
        print()


def search_acc():
    print("Searching account...")
    search = input("Enter website to search: ")
    found = False

    for account in accounts:
        if account["website"].lower() == search.lower():
            print("Website:", account["website"])
            print("Username:", account["username"])
            print("Password:", account["password"])
            found = True

    if found == False:
            print("Website Not found!")


def gen_pass():
    print("Generating password...")

    length = int(input("Enter password length: "))

    while length < 8:
        print("Password length must be at least 8 characters.")
        length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(length - 4):
        password += random.choice(characters)

    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    print("Generated password:", password)

    return password


def upd_pass():
    print("Updating password...")

    website = input("Enter website to update: ")

    found = False

    for account in accounts:
        if account["website"].lower() == website.lower():
            print("Account found!")

            print("1. Enter password manually")
            print("2. Generate password")

            choice = int(input("Choose an option: "))

            if choice == 1:
                new_password = input("Enter new password: ")

            elif choice == 2:
                new_password = gen_pass()

            else:
                print("Invalid option!")
                return

            account["password"] = new_password

            print("Password updated successfully!")

            found = True
            break

    if found == False:
        print("Website not found!")




def del_acc():
    print("Deleting account...")
def goodbye():
    print("Goodbye!")




while True:

    print("1. Add account") 
    print("2. View accounts") 
    print("3. Search account") 
    print("4. Generate password") 
    print("5. Update password") 
    print("6. Delete account") 
    print("7. Exit") 

    response = int(input("Enter your action: "))

    if response == 1:
        add_acc()

    elif response == 2:
        view_acc()

    elif response == 3:
        search_acc()

    elif response == 4:
        gen_pass()

    elif response == 5:
        upd_pass()

    elif response == 6:
        del_acc()

    elif response == 7:
        goodbye()
        break
    else:
        print("Invalid Action")