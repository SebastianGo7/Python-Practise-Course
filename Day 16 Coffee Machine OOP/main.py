from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def user_interaction():

    # creating the coffee maker, the menu and the money machine
    my_coffee_maker = CoffeeMaker()
    my_menu = Menu()
    my_money_machine = MoneyMachine()

    currently_attending = True
    while currently_attending:

        chosen_coffee_type = input(f"What would you like? ({my_menu.get_items()}) ").lower()

        if chosen_coffee_type == "report":
            # creating the report
            my_coffee_maker.report()
            my_money_machine.report()

        elif chosen_coffee_type == "off":
            currently_attending = False

        else:
            my_menu_item = my_menu.find_drink(chosen_coffee_type)

            if my_coffee_maker.is_resource_sufficient(my_menu_item):
                # proceeding to coin processing as sufficient resources

                if my_money_machine.make_payment(my_menu_item.cost):
                    # coffee can be made now
                    my_coffee_maker.make_coffee(my_menu_item)


user_interaction()



