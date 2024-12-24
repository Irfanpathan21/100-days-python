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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:  # Corrected comparison here
            print(f"Sorry there isn't enough {item}")
            return False
    return True

def process_coins():
    print("Please Enter Coins")
    total = int(input("How Many Quarters?")) * 0.25
    total += int(input("How Many Dimes?")) * 0.1  # Fixed the spelling of "dimes"
    total += int(input("How Many Nickels?")) * 0.05
    total += int(input("How Many Pennies?")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)  # Fixed assignment of change
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost  # Only add the cost of the drink to profit
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice,drink["ingredients"])

