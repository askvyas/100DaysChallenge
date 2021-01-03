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
coin_values={
    "quarters": 0.25,
    "dimes":0.1,
    "nickles":0.05,
    "pennies":0.01

}
current_cash=0

# Step 3: Functions for each case of the choice of the user
def get_report():
    global  current_cash
    global resources
    print(f"Water:" + f"{resources["water"]}")
    print(f"Coffee: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money {current_cash}")


def check_resources(coffee_usr):
    if resources["water"] > MENU[coffee_usr]["ingredients"]["water"] and resources["milk"] > MENU[coffee_usr]["ingredients"]["milk"] and resources["coffee"] > MENU[coffee_usr]["ingredients"]["coffee"]:
        return True
    else:
        return False
def check_price(coins,coffee_usr):
    if coins >= MENU[coffee_usr]["cost"]:
        return True
    else:
        return False






# Step2: Lets write a function to get coffee

def get_coffee():
    # Step1: Take user input asking what is his choice for coffee
    coffee_usr = input("What would you like ?")
    if coffee_usr== "report":
        get_report()
        get_coffee()
    elif coffee_usr== "off":
        return
    else:
        if check_resources(coffee_usr):



