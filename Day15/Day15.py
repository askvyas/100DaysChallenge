MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coin_values = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01

}
current_cash = 0


# Step 3: Functions for each case of the choice of the user
def get_report():
    """" Function that calculates current resources left and prints it"""
    global current_cash
    global resources
    print(f"Water:" + str( resources["water"]))
    print(f"Coffee: " +  str(resources["milk"]))
    print(f"Coffee: " + str(resources["coffee"]))
    print(f"Money {current_cash}")


def check_resources(coffee_usr):
    """" Function that checks current resources left and resources required to make the coffee"""
    if coffee_usr=="espresso":
        if resources["water"] > MENU[coffee_usr]["ingredients"]["water"] and resources["coffee"] > MENU[coffee_usr]["ingredients"]["coffee"]:
            return True


    elif resources["water"] > MENU[coffee_usr]["ingredients"]["water"] and resources["milk"] >  MENU[coffee_usr]["ingredients"]["milk"] and resources["coffee"] > MENU[coffee_usr]["ingredients"]["coffee"]:
        return True
    else:
        return False


def low_resources(coffee_user):
    if resources["water"] > MENU[coffee_user]["ingredients"]["water"]:
        print("Sorry there is not not enough water")
    elif resources["milk"] > MENU[coffee_user]["ingredients"]["milk"]:
        print("Sorry there is not not enough milk")
    elif resources["coffee"] > MENU[coffee_user]["ingredients"]["coffee"]:
        print("Sorry there is not not enough coffee")


def check_price(coins, coffee_usr):
    """" Compares price list of coffe and the currency given by the user """
    if coins >= MENU[coffee_usr]["cost"]:
        return True
    else:
        return False


def get_coins():
    """" Function that gets takes input of how many coins the user has and returns them as a list"""
    l = []
    print()
    l.append(float(input("How many Quarters? ")))
    l.append(float(input("How many Dimes? ")))
    l.append(float(input("How many Nickels? ")))
    l.append(float(input("How many Pennies? ")))
    return l


def get_sum(l):
    return l[0] * 0.25 + l[1] * 0.1 + l[2] * 0.05 + l[2] * 0.01


def deduct_resources(coffee_usr):
    global current_cash
    global resources
    if(coffee_usr!="espresso"):
        resources["milk"] = resources["water"] - MENU[coffee_usr]["ingredients"]["milk"]

    current_cash = current_cash + MENU[coffee_usr]["cost"]
    resources["water"] = resources["water"] - MENU[coffee_usr]["ingredients"]["water"]
    resources["coffee"] = resources["water"] - MENU[coffee_usr]["ingredients"]["coffee"]


# Step2: Lets write a function to get coffee

def get_coffee():
    # Declare resources and current_cash as global to make changes globally in those 2 variables
    global current_cash
    global resources
    # Step1: Take user input asking what is his choice for coffee
    coffee_usr = input("What would you like ?")
    if coffee_usr == "report":
        get_report()
        get_coffee()
        get_coffee()
    elif coffee_usr == "off":
        return
    else:
        if check_resources(coffee_usr):
            user_coins = get_coins()
            total_money = get_sum(user_coins)
            if check_price(total_money, coffee_usr):
                change = total_money - MENU[coffee_usr]["cost"]
                deduct_resources(coffee_usr)

                print(f"Her is ${change} in change")
                print(f"Here is your ☕️ {coffee_usr} Enjoy")
                get_coffee()
            else:
                print("Sorry that's not enough money. Money refunded")
                get_coffee()


        else:
            low_resources(coffee_usr)
            get_coffee()

get_coffee()

# TODO 1.Order  a coffe and Enjoy
