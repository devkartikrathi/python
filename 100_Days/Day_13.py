# COFFEE MACHINE

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "income": 0
}

def espresso():
    if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
        print("Not enough water at the time.")
    elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
        print("Not enough coffee at the time. ")
    else:
        return (True)

def latte():
    if resources["water"] < MENU["latte"]["ingredients"]["water"]:
        if resources["water"] > MENU["espresso"]["ingredients"]["water"]:
            t = input("Not enough water for latte at the time, would you like try anything else. (Y/N) : ").lower()
            if t == "y":
                inpt(resources)
            else:
                print("Sorry for the inconvinence")    
    elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
        print("Not enough coffee at the time. ")
    elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        print("Not enough milk at the time. ")    
    else:
        return (True)

def cappuccino():
    if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
        if resources["water"] > MENU["latte"]["ingredients"]["water"] or resources["water"] > MENU["espresso"]["ingredients"]["water"]:
            t = input("Not enough water for cappuccino at the time, would you like try anything else. (Y/N) : ").lower()
            if t == "y":
                inpt(resources)
            else:
                print("Sorry for the inconvinence")
    elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
        print("Not enough coffee at the time. ")
    elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
        print("Not enough milk at the time. ")    
    else:
        return (True)        

def inpt(resources):
    x = input("What would you like to have? (Espresso/Latte/cappuccino) : ").lower()
    
    if x == "report":
        print(resources)
        inpt(resources)

    else:        
        if x == "espresso":
            if espresso() == True:
                y = int(input("Enter number of ten rupee note :"))
                z = int(input("Enter five rupee note : "))
                total_money = (y*10) + (z*5)
                if total_money >= MENU["espresso"]["cost"]:
                    change = total_money - MENU["espresso"]["cost"]
                    resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                    resources["income"] += MENU["espresso"]["cost"]
                    print("Enjoy your Espresso.")
                    print(f"Your change is {change}")
                    inpt(resources)
                else:
                    print("Please give Rs. 15 for Espresso") 
                    inpt(resources)        

        elif x == "latte":
            if latte() == True:
                y = int(input("Enter number of ten rupee note :"))
                z = int(input("Enter five rupee note : "))
                total_money = (y*10) + (z*5)
                if total_money >= MENU["latte"]["cost"]:
                    change = total_money - MENU["latte"]["cost"]
                    resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                    resources["income"] += MENU["latte"]["cost"]
                    print("Enjoy your Latte.")
                    print(f"Your change is {change}")
                    inpt(resources)
                else:
                    print("Please give Rs. 25 for Latte")
                    inpt(resources)

        elif x == "cappuccino":
            if cappuccino() == True:
                y = int(input("Enter number of ten rupee note :"))
                z = int(input("Enter five rupee note : "))
                total_money = (y*10) + (z*5)
                if total_money >= MENU["cappuccino"]["cost"]:
                    change = total_money - MENU["cappuccino"]["cost"]
                    resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                    resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                    resources["income"] += MENU["cappuccino"]["cost"]
                    print("Enjoy your Cappuccino.")
                    print(f"Your change is {change}")
                    inpt(resources)
                else:
                    print("Please give Rs. 30 for Cappuccino")
                    inpt(resources)

        else : 
            print("Enter a valid choice.")
            inpt(resources)    

inpt(resources)

'''
root = tk.Tk
frame = tk.Frame
frame.pack()
espresso_button = tk.Button(frame,
    text = "Espresso",
    fg = "brown",
    command = inpt)

latte_button = tk.Button(frame,
    text = "Latte",
    fg = "brown",
    command = inpt)

cappuccino_button = tk.Button(frame,
    text = "Cappuccino",
    fg = "brown",
    x = "cappuccino"
    command = inpt)
    '''