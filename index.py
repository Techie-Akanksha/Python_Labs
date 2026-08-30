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

def view_acc():
    print("Showing account...")
    for account in accounts:
        print(account)


def search_acc():
    print("Searching account...")
def gen_pass():
    print("Generating password...")
def upd_pass():
    print("Updating password...")
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