
from Ingredients_Dictionary import MENU, resources
import ASCII_Art

print(ASCII_Art.asciiArt)

global_variable_coffee_machine_money = 0.0


def process_coins(coffee_type):
    """Gets Coffee Type, requests coins from user, calculates if enough,
    if calls function to deduct coins and records global coffeeMachineMoney"""

    global global_variable_coffee_machine_money

    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    money_entered = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if money_entered < MENU[coffee_type]["cost"]:
        print("Sorry that is not enough money. Money refunded.")

    else:
        transaction_sufficient(coffee_type)

        change = round(money_entered - MENU[coffee_type]["cost"], 2)
        print(f"Here is ${change} in change.")
        print(f"Here we go ☕. Enjoy your {coffee_type}️.")

        global_variable_coffee_machine_money += MENU[coffee_type]["cost"]


def check_resources(coffeetype):
    """Function checks if there are enough resources available for the order"""

    if int((resources['water'])) < (int(MENU[coffeetype]["ingredients"]["water"])):
        print("Sorry, there is not enough water available.")
        return False

    if (int(resources['milk'])) < (int(MENU[coffeetype]["ingredients"]["milk"])):
        print("Sorry, there is not enough milk available.")
        return False

    if int(resources['coffee'] < MENU[coffeetype]["ingredients"]["coffee"]):
        print("Sorry, there is not enough coffee available.")
        return False

    return True


def transaction_sufficient(coffee_type):
    """Function deducts resources depending on coffee Type"""
    resources['water'] = resources['water'] - MENU[coffee_type]["ingredients"]["water"]
    resources['milk'] = resources['milk'] - MENU[coffee_type]["ingredients"]["milk"]
    resources['coffee'] = resources['coffee'] - MENU[coffee_type]["ingredients"]["coffee"]


def report_function():
    """Function prints out report if requested"""
    print (f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \ncoffee: {resources['coffee']}g")
    print (f"Money: ${global_variable_coffee_machine_money}")


def attending_users():
    """Initial user interaction, and report and off choices"""
    currently_attending = True
    while currently_attending:

        user_coffee_choice = input("What would you like? (espresso / latte / cappuccino) ").lower()
        if user_coffee_choice == "report":
            report_function()

        elif user_coffee_choice == "off":
            currently_attending = False
            break

        elif check_resources(user_coffee_choice):
            process_coins(user_coffee_choice)


attending_users()
# calling the coffee machine starting function

