from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_is_on = True

while machine_is_on:
    drink = input(f"name of drink {menu.get_items()} ")
    if drink == "report":
        money_machine.report()
        coffee_maker.report()
    elif drink == "off":
        machine_is_on = False
    else:
        chosen_drink = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(chosen_drink) and money_machine.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee(chosen_drink)








