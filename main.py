from coffee_machine_data import MENU,resources
from art import logo

def calculate_money(quarters,dimes,nickles,pennies):
    """for calculating the total money that the user inserted on coffe machine."""
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

def check_money(order, t_money):
    """check whether is the entered money is enough for wrapping the cost or not."""
    if MENU[order]['cost'] >= t_money:
       return False
    else:
        return True

def check_ingredients(order_ing):
    """check whether the ingredients are enough or not."""
    for key_order in order_ing:
        if resources[key_order] < order_ing [key_order]:
            return ["False",key_order]
    return ["True"]

def get_change(t_money,order_cost):
    """get the rest of the inserted money. """
    return t_money - order_cost

def reduce_resources(order_ing):
    for key_ing in order_ing:
        if "water" == key_ing:
            resources['water'] -= order_ing[key_ing]
        elif "milk" == key_ing:
            resources['milk'] -= order_ing[key_ing]
        elif "coffee" == key_ing:
            resources['coffee'] -= order_ing[key_ing]

def coffee_machine():
    print(logo)
    profit = 0
    is_on = True
    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino):").lower()
        while order != "espresso" and order != "latte" and order != "cappuccino" and order != "off" and order!= "report":
            order = input("What would you like? (espresso/latte/cappuccino):").lower()
        if order == "off":
            is_on = False
        elif order == "report":
            print(f"Water: {resources['water']} ml")
            print(f"Milk: {resources['milk']} ml")
            print(f"Coffee: {resources['coffee']} g")
            print(f"Money: $ {profit}")
        else:
            check_ingredients_list = check_ingredients(MENU[order]['ingredients'])

            if check_ingredients_list[0] == "True":
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("how many nickels?: "))
                pennies = int(input("How many pennies?: "))
                total_money = calculate_money(quarters,dimes,nickles,pennies)
                money_is_valid = check_money(order, total_money)
                if money_is_valid:
                    reduce_resources(MENU[order]['ingredients'])
                    profit+=MENU[order]['cost']
                    print(f"Here is ${round(get_change(total_money,MENU[order]['cost']),2)} in change.")
                    print(f"Here is your {order} ☕️. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry there is not enough {check_ingredients_list[1]}.")



coffee_machine()