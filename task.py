import random
import string


# PASSWORD MANAGER

print("=" * 75)
print("                         PASSWORD MANAGER")
print("=" * 75)
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
    print("Showing accounts...")

    if len(accounts) == 0:
        print("No accounts found.")
        print()
        return

    # enumerate() gives us the account number and account data
    for i, account in enumerate(accounts, start=1):
        print("Account", i)
        print("Website:", account["website"])
        print("Username:", account["username"])
        print("Password:", account["password"])
        print()


def search_acc():
    print("Searching account...")

    if len(accounts) == 0:
        print("No accounts found.")
        print()
        return

    search = input("Enter website to search: ")

    found = False

    for account in accounts:
        if account["website"].lower() == search.lower():
            print("Website:", account["website"])
            print("Username:", account["username"])
            print("Password:", account["password"])
            print()

            found = True

    if found == False:
        print("Website not found!")


def gen_pass():
    print("Generating password...")

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 8:
                print("Password length must be at least 8 characters.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ""

    # Guarantee at least one of each character type
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    # Fill the remaining characters
    for i in range(length - 4):
        password += random.choice(characters)

    # Shuffle the password
    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    # website = input("Enter website for this password: ")
    # for account in accounts:
    #     if account["website"].lower() == website.lower():
    #             account["password"] = password
    #             print("Password updated for", website)
    #             break
    #     else:
    #         print("No account found for", website)
    #         print("You can add this password to a new account.")

    print("Generated password:", password)

    return password


def upd_pass():
    print("Updating password...")

    if len(accounts) == 0:
        print("No accounts found.")
        print()
        return

    website = input("Enter website to update: ")

    found = False

    for account in accounts:
        if account["website"].lower() == website.lower():
            print("Account found!")

            print("1. Enter password manually")
            print("2. Generate password")

            while True:
                try:
                    choice = int(input("Choose an option: "))

                    if choice not in [1, 2]:
                        print("Please choose 1 or 2.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid number.")

            if choice == 1:
                new_password = input("Enter new password: ")

            elif choice == 2:
                new_password = gen_pass()

            account["password"] = new_password

            print("Password updated successfully!")

            found = True
            break

    if found == False:
        print("Website not found!")


def del_acc():
    print("Deleting account...")

    if len(accounts) == 0:
        print("No accounts found.")
        print()
        return

    website = input("Enter website to delete: ")

    found = False

    for account in accounts:
        if account["website"].lower() == website.lower():
            print("Account found!")

            confirm = input(
                "Are you sure you want to delete this account? (y/n): "
            )

            if confirm.lower() == "y":
                accounts.remove(account)
                print("Account deleted successfully!")

            else:
                print("Deletion cancelled.")

            found = True
            break

    if found == False:
        print("Website not found!")


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

    try:
        response = int(input("Enter your action: "))

    except ValueError:
        print("Please enter a number.")
        print()
        continue

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

    print()

