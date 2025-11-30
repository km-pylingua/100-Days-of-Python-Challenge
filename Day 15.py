#TODO-1: figure out dictionaries for water, coffee, etc. 
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources_spent=resources.copy()

current_resources = {
    "water": resources_spent["water"],
    "milk": resources_spent["milk"],
    "coffee": resources_spent["coffee"],
}

total_spent=0

def update_resources(order):
    water = menu[order]["ingredients"]["water"]
    milk = menu[order]["ingredients"]["milk"]
    coffee = menu[order]["ingredients"]["coffee"]
    resources_spent["water"] = resources_spent["water"] - water
    resources_spent["milk"] = resources_spent["milk"] - milk
    resources_spent["coffee"] = resources_spent["coffee"] - coffee

def add_to_total(current_total):
    global total_spent
    total_spent=total_spent + current_total
    return total_spent

def print_report():
    print(f"Water:" {resources_spent["water"]}")
    print(f"Milk: {resources_spent["milk"]}")
    print(f"Coffee: {resources_spent["coffee"]}")
    print(f"Money:", {total_spent})

def coin_counter(order):
    current_spent=0
    keep_running=True
    while keep_running:
        quarters=float(input("How many quarters? "))*25
        dimes=float(input("How many dimes? "))*10
        nickles=float(input("How many nickles? "))*5
        pennies=float(input("How many pennies? "))
        money_inserted=(quarters+dimes+nickles+pennies)/100
        item_price=menu[order]["cost"]
        current_spent=current_spent+money_inserted
        if item_price>current_spent:
            print("Please insert more money.")
        else:
            change_owed=current_spent-item_price
            print(f"Here is ${change_owed:.2f} in change.")
            add_to_total(item_price)
            keep_running=False

#TODO-2: create a loop that continuously asks for what the user would like called coffee_machine_on
#TODO-3: make user input what they would like to run
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "espresso" or order == "latte" or order == "cappuccino":
        coin_counter(order)
        update_resources(order)
        print(f"Here is your {order}. Enjoy!")
    elif order == "report":
        print_report()
    else:
        print("Error. Please type in a valid order.")

#TODO-4: if user types report, create a functiont that will display resources available 

#TODO-5: create a way to keep track of resources that are continuously changed while loop continues

#TODO-6: create a way to keep track of how much money the user inputs totals up to

#TODO-7: subtracct the amount the coffee costs from the total money the user inputed

#TODO-8: request how much quarters, dimes, nickles and pennies the user wants to input and store the variables

#TODO-9: find what the user is asking for in the MENU and if it matches, subtract the amount of water/milk/coffee from resources

#TODO-10: display change after resources and money subtracted

#TODO-11: display "here is your {selected drink}" with emoji enjoy!

#TODO-12: if input is "off", end program/loop