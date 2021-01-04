from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def drink_coffee():

    usr_menu=Menu()
    usr_coffee=CoffeeMaker()
    usr_mon=MoneyMachine()

    print(usr_menu.get_items())

    user_inp = input("What would you like to have? ")
    if user_inp == "report":
        usr_coffee.report()
    elif user_inp == "off":
        return
    else:
        c_d=usr_menu.find_drink(user_inp)
        if c_d != None:
            if usr_coffee.is_resource_sufficient(user_inp):
                usr_mon.make_payment(c_d.cost)






