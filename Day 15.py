#TODO-1: figure out dictionaries for water, coffee, etc. 
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

#TODO-2: create a loop that continuously asks for what the user would like called coffee_machine_on

#TODO-3: make user input what they would like to run

#TODO-4: if user types report, create a functiont that will display resources available 

#TODO-5: create a way to keep track of resources that are continuously changed while loop continues

#TODO-6: create a way to keep track of how much money the user inputs totals up to

#TODO-7: subtracct the amount the coffee costs from the total money the user inputed

#TODO-8: request how much quarters, dimes, nickles and pennies the user wants to input and store the variables

#TODO-9: find what the user is asking for in the MENU and if it matches, subtract the amount of water/milk/coffee from resources

#TODO-10: display change after resources and money subtracted

#TODO-11: display "here is your {selected drink}" with emoji enjoy!

#TODO-12: if input is "off", end program/loop