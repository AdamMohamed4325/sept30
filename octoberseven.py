balance = 0

while True:

    print(" Welcome to the Byte & Brew tech cafe!")
    print(" We have a Selection of 3 very delicious items on our menu.")
    print(" What can i get for you today.")
    print(" 1 Pineapple Refresher $2.78.")
    print(" 2 Caramel Latte $6.54.")
    print(" 3 Chocolate Drizzled pancakes $12.99.")

    choice = input("what would you like? ")

    if choice == "1":
        balance = balance + 2.78
        print("Great choice, that will be $2.78.")

    elif choice == "2":
        balance = balance + 6.54
        print("That will be $6.54.")

    elif choice == "3":
        balance = balance + 12.99
        print("Thats our most sold item, i hope you enjoy it.")

    else:
        print("Sorry please choose an item on the menu.")
        continue

    print("Your balance is now $", balance)

    while True:

        choice = input("Enter another item or enter 4 to checkout: ")

        if choice == "1":
            balance = balance + 2.78
            print("You added a Pineapple Refresher.")
            print("Your balance is now $", balance)

        elif choice == "2":
            balance = balance + 6.54
            print("You added a Caramel Latte.")
            print("Your balance is now $", balance)

        elif choice == "3":
            balance = balance + 12.99
            print("You added Chocolate Drizzled pancakes.")
            print("Your balance is now $", balance)

        elif choice == "4":
            print("Your final balance is $", balance)
            print("Thank you for visiting Byte & Brew!")
            break

        else:
            print("Sorry please choose an item on the menu.")

    break
