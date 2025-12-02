#TODO-2: create a loop that continuously asks for what the user would like called coffee_machine_on
#TODO-3: make user input what they would like to run
#TODO-12: if input is "off", end program/loop
total_spent=0
 #TODO-5: create a way to keep track of resources that are continuously changed while loop continues
resources_spent = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coffee_pot_on=True
while coffee_pot_on==True:
    order = input("What would you like? (espresso/latte/cappuccino): ")

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

    def update_resources(drink):
        #TODO-9: find what the user is asking for in the MENU and if it matches, subtract the amount of water/milk/coffee from resources
        water = menu[drink]["ingredients"]["water"]
        milk = menu[drink]["ingredients"]["milk"]
        coffee = menu[drink]["ingredients"]["coffee"]
        for key, value in resources_spent.items():
            resources_spent[key] = resources_spent[key] - menu[drink]["ingredients"][key]
            if resources_spent[key] < 0:
                print(f"You do not have enough {key}.")
                resources_spent[key] = resources_spent[key] + menu[drink]["ingredients"][key]
                return False

    def add_to_total(current_total):
        #TODO-6: create a way to keep track of how much money the user inputs totals up to
        global total_spent
        total_spent=total_spent + current_total
        return total_spent

    def print_report():
        #TODO-4: if user types report, create a functiont that will display resources available 
        print("Water:", resources_spent["water"])
        print("Milk:", resources_spent["milk"])
        print("Coffee:", resources_spent["coffee"])
        print(f"Money:", "$",total_spent)

    def coin_counter(drinks):
        current_spent=0
        keep_running=True
        while keep_running:
            #TODO-8: request how much quarters, dimes, nickles and pennies the user wants to input and store the variables
            quarters=float(input("How many quarters? "))*25
            dimes=float(input("How many dimes? "))*10
            nickles=float(input("How many nickles? "))*5
            pennies=float(input("How many pennies? "))
            money_inserted=(quarters+dimes+nickles+pennies)/100
            item_price=menu[drinks]["cost"]
            #TODO-7: subtract the amount the coffee costs from the total money the user inputed
            current_spent=current_spent+money_inserted
            if item_price>current_spent:
                print("Please insert more money.")
            else:
                change_owed=current_spent-item_price
                #TODO-10: display change after resources and money subtracted
                print(f"Here is ${change_owed:.2f} in change.")
                add_to_total(item_price)
                keep_running=False

    if order == "off":
        coffee_pot_on=False
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        enough_resources = update_resources(order)
        if enough_resources == False:
            continue
        else:
            coin_counter(order)
            #TODO-11: display "here is your {selected drink}" with emoji enjoy!
            print(f"Here is your {order} ☕. Enjoy!")
    elif order == "report":
        print_report()
    else:
        print("Error. Please type in a valid order.")


#TODO-13: if resource is below required amount of order requested, tell user there is not enough of the resource to make the drink






