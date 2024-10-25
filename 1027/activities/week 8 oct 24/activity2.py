def add_funds(accounts):
    # This function should ask for a username and an amount to add.
    # If the user exits, it should update that user's account.
    # If the user does not exist, it should add them and set their account amount to the input value.

    user = input("Input username: ").lower()
    amount = float(input("Amount to add: $"))
    
    account_found = 0

    for account in accounts:
        if account == user:
            account_found = 1
            accounts[user] = amount
            print(accounts[user])
            print("$%.2f added successfully!\n" % amount)
    if account_found == 0:
        accounts[user] = 0
        accounts[user] = accounts[user] + amount
        print("Added new user with $%.2f!\n" % amount)
            

def print_pages(accounts):
    # This function should ask for a username and an amount of pages to print.
    # If the user has enough money in their account, subtract it from their account and
    # output "Print Successful".
    # If the user does not have enough money, output the error "Error: Insufficient Funds".
    # If the user does not exist, output the error "Error: Unknown User".
    # It should cost 25 cents per page.

    user = input("Input username: ").lower()
    amount = int(input("Pages to print: "))

    user_found = 0
    cost = amount * 0.25
    
    for account in accounts:
        if account == user:
            user_found = 1
            if accounts[user] >= cost:
                accounts[user] = accounts[user] - cost
                print("Print Successfull\n")
            else:
                print("Error: Insufficient Funds\n")

    if user_found == 0:
        print("Error: Unknown User\n")


def list_funds(accounts):
    # This function should ask for a username and print the current amount of funds the user has.
    # If the user does not exist, output the error "Error: Unknown User".

    user = input("Input username: ").lower()
    user_found = 0

    for account in accounts:
        if account == user:
            user_found = 1
            print("Amount: $%.2f\n" % accounts[user])
    if user_found == 0:
        print("Error: Unknown User\n")


def print_menu():
    print("Select an option:")
    print("1) Add funds")
    print("2) Print")
    print("3) List funds")

def main():
    accounts = {"alice": 1.32,
                "bob": 0.0,
                "charlie": 3.50,
                "eve": 1337.42}
    while True:
        print_menu()
        menu_item = int(input("> "))
        if menu_item == 1:
            add_funds(accounts)
        elif menu_item == 2:
            print_pages(accounts)
        elif menu_item == 3:
            list_funds(accounts)
        else:
            break

main()