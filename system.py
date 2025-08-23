from datetime import datetime
import random

balance = 0  # Always PLN

def log_operation(operation_type, currency, amount, balance):
    with open("operations.txt", "a") as file:
        file.write(f"[{datetime.now()}] {operation_type.upper()} - {currency.upper()} - {amount} - Balance: {balance} PLN\n")

def generate_receipt(operation_type, card_last4, customer_name, requested, fee, total): # I got small help from AI ;)
    terminal_id = random.randint(10000000, 99999999)
    sequence_id = random.randint(1000, 9999)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("operations.txt", "a") as file:
        file.write("\n-------------------------------\n")
        file.write("         ATM TRANSACTION\n")
        file.write("-------------------------------\n")
        file.write(f"TERMINAL #       {terminal_id}\n")
        file.write(f"SEQUENCE #       {sequence_id}\n")
        file.write(f"DATE             {now}\n")
        file.write(f"CARD NUMBER      XXXXXXXXXXXX{card_last4}\n")
        file.write(f"CUSTOMER NAME    {customer_name}\n")
        file.write("-------------------------------\n")
        file.write(f"{operation_type.upper()} AMOUNT     {requested} PLN\n")
        file.write(f"TERMINAL FEE          {fee} PLN\n")
        file.write(f"TOTAL AMOUNT        {total} PLN\n")
        file.write("-------------------------------\n\n")


def deposit():
    global balance
    print("\n----------Deposit----------\n")
    currancy = input("Please select your currency: USD/PLN/EUR: ").upper()
    print("1 USD = 3.64 PLN\n1 PLN = 1.00 PLN\n1 EUR = 4.26 PLN")

    if currancy == "USD":
        amount = float(input("\nPlease add (USD): "))
        converted = amount * 3.64
        fee = 2.50
    elif currancy == "PLN":
        amount = float(input("\nPlease add (PLN): "))
        converted = amount
        fee = 1.25
    elif currancy == "EUR":
        amount = float(input("\nPlease add (EUR): "))
        converted = amount * 4.26
        fee = 1.75
    else:
        print("Something went wrong!")
        return

    balance += converted - fee

    print(f"Deposited: {converted} PLN (Fee: {fee} PLN)")
    print(f"Current balance: {balance} PLN\n")

    log_operation("deposit", currancy, amount, balance)
    generate_receipt("deposit", "5698", "ELVIN BABANLI", amount, fee, converted)


def withdraw():
    global balance
    print("\n----------Withdraw----------\n")
    currancy = input("Please select your currency: USD/PLN/EUR: ").upper()
    print("1 USD = 3.64 PLN\n1 PLN = 1.00 PLN\n1 EUR = 4.26 PLN")

    if currancy == "USD":
        amount = float(input("\nPlease withdraw (USD): "))
        converted = amount * 3.64
        fee = 0.50
    elif currancy == "PLN":
        amount = float(input("\nPlease withdraw (PLN): "))
        converted = amount
        fee = 0.25
    elif currancy == "EUR":
        amount = float(input("\nPlease withdraw (EUR): "))
        converted = amount * 4.26
        fee = 0.75
    else:
        print("Something went wrong!")
        return

    total = converted + fee
    if total > balance:
        print("Insufficient funds!\n")
        return

    balance -= total

    print(f"Withdrawn: {converted} PLN (Fee: {fee} PLN)")
    print(f"Current balance: {balance} PLN\n")

    log_operation("withdraw", currancy, amount, balance)
    generate_receipt("withdraw", "5698", "ELVIN BABANLI", amount, fee, total)


def check_balance():
    print("\n----------Check balance----------\n")
    print(f"Your available balance is: {balance} PLN\n")


def transfer():
    global balance
    print("\n----------Transfer----------\n")
    option = int(input("Options: 1.Bank Santander / 2.Bank Polska : "))

    if option == 1:
        fee = 4.99
        bank = "Santander"
    elif option == 2:
        fee = 5.99
        bank = "Polska"
    else:
        print("Something went wrong!")
        return

    amount = float(input("\nPlease add amount (PLN): "))
    total = amount + fee

    if total > balance:
        print("Insufficient funds!\n")
        return

    balance -= total

    print(f"Transfer to Bank {bank} successful.")
    print(f"Current balance: {balance} PLN\n")

    log_operation("transfer", "PLN", amount, balance)
    generate_receipt("transfer", "5698", "ELVIN BABANLI", amount, fee, total)


def options():
    print("\n----------Options----------\nComing soon...\n")


def quit_program():
    print("\nExiting program... Bye!\n")
    exit()


while True:
    print("\n========== Welcome to ATM ==========\n")
    try:
        pin = int(input("Please enter your PIN: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue

    if pin == 1234 or pin == 1111:
        while True:
            print("------ Main Menu ------")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transfer")
            print("5. Options")
            print("6. Exit")
            try:
                select = int(input("Select an option: "))
            except ValueError:
                print("Invalid input. Try again.\n")
                continue

            if select == 1:
                deposit()
            elif select == 2:
                withdraw()
            elif select == 3:
                check_balance()
            elif select == 4:
                transfer()
            elif select == 5:
                options()
            elif select == 6:
                quit_program()
            else:
                print("Invalid selection!\n")
    else:
        print("Wrong PIN. Try again.\n")
