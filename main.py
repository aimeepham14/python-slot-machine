MAX_LINES = 3

def deposit():
    while True: 
        amount = input("What would you like to deposit? $")
        #making sure that the user types in a positive whole valid number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

#collecting the bet from the users
def get_number_of_lines():
    while True: 
        lines = input("What would you like to deposit? $")
        #making sure that the user types in a positive whole valid number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount



def main ():
    balance = deposit()

main()