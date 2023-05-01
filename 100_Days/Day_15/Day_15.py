# using PRETTY_TABLE
'''from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Names", ["Sid", "Billy", "Sumit"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)'''

#---------------------------------------------------------------------------------------------------------------#

# COFFEE MACHINE (Part - 2)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have {options} : ") 
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) == True:
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)