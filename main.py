#still in development

def start():
    start = input("press any key to start")
    print()
    print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ LYCDONALD ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
    print()
    print(" --- --- --- --- please type the number of your choice --- --- --- --- ")
    print()

#ask the user where do they want to eat
def dinePlace():
    while True:
        print("Where do you want to eat?")
        print("(1) Dine In")
        print("(2) Take Out")
        print()
        dinePlaceChoice = input("Choice: ")
        if(dinePlaceChoice == "1"):
            print("Place: Dine In")
            print()
            paymentChoice()
            break
        elif(dinePlaceChoice == "2"):
            print("Place: Take Out")
            print()
            paymentChoice()
            break
        else:
            print("Invalid choice, please choose again")
            print()

#ask the user how will they pay
def paymentChoice():
    while True:
        print("How would you like to pay?")
        print("(1) Cash")
        print("(2) Card")
        print()
        paymentRestChoice = input("Choice: ")
        if(paymentRestChoice == "1"):
            print("Payment: Cash")
            print()
            mainMenu()
            break
        elif(paymentRestChoice == "2"):
            print("Payment: Card")
            print()
            mainMenu()
            break
        else:
            print("Invalid choice, please choose again")
            print()

#displays the mainmenu
def mainMenu():
    while True:
        print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ MAIN MENU ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
        print()
        print(" --- --- --- --- please type the number of your choice --- --- --- --- ")
        print()
        print("(1) Main Dish")
        print("(2) Burgers")
        print("(3) Fries and Add ons")
        print("(4) Beverages")
        print("(5) Pasta")
        print()

        mainMenuChoice = input("Choice: ")
        if(mainMenuChoice == "1"):
            print("Meal: Main Dish")
            print()
            print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ MAIN DI SH MENU ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
            print()
            print(" --- --- --- --- please type the number of your choice --- --- --- --- ")
            print()
            comboMealsMenu()
            break
        elif(mainMenuChoice == "2"):
            print("Meal: Burgers")
            print()
            print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄ BURGERS ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
            print()
            print(" --- --- --- --- please type the number of your choice --- --- --- --- ")
            print()
            burgerMealsMenu()
            break
        elif (mainMenuChoice == "3"):
            print("Meal: Fries and Add Ons")
            print()
            print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ FRIES AND ADD ONS ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
            print()
            print(" --- --- --- --- please type the number of your choice --- --- --- --- ")
            print()
            friesMealsMenu()
            break
        elif (mainMenuChoice == "4"):
            print("Meal: Beverages")
            print()
            print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ BEVERAGES ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
            print()
            print(" --- --- --- --- please type the number of your choice --- --- --- --- ")
            print()
            beverageMealsMenu()
            break
        elif (mainMenuChoice == "5"):
            print("Meal: Pasta")
            print()
            print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ PASTA ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
            print()
            print(" --- --- --- --- please type the number of your choice --- --- --- --- ")
            print()
            pastaMealsMenu()
            break
        else:
            print("Invalid choice, please choose again")
            print()

#displays the combo meal menu section
def comboMealsMenu():
    cld = 200
    cln = 150
    cf = 150
    mps = 100
    total = 0
    while True:
        print("    MAIN DISH")
        print()
        print("(1) Chicken LycDonald - ₱200")
        print("(2) Chicken LycNuggets - ₱150")
        print("(3) Chicken Fillet - ₱150")
        print("(4) Mushroom Pepper Steak - ₱100")
        print()
        comboMealsMenuChoice = input("Choice: ")

        if(comboMealsMenuChoice == "1"):
            print("Order: Chicken LycDonald")
            quantity = int(input("Quantity: "))
            total += quantity * cld
            print("Total:" + str(total))
            break
        elif (comboMealsMenuChoice == "2"):
            print("Order: Chicken LycNuggets")
            quantity = int(input("Quantity: "))
            total += quantity * cln
            print("Total:" + str(total))
            break
        elif (comboMealsMenuChoice == "3"):
            print("Order: Chicken Fillet")
            quantity = int(input("Quantity: "))
            total += quantity * cf
            print("Total:" + str(total))
            break
        elif (comboMealsMenuChoice == "4"):
            print("Order: Mushroom Pepper Steak")
            quantity = int(input("Quantity: "))
            total += quantity * mps
            print("Total:" + str(total))
            break
        else:
            print("Invalid choice, please choose again")
            print()

#displays the burger meal menu section
def burgerMealsMenu():
    bigmac = 150
    crispyChicken = 130
    spicyChicken = 100
    dcheeseburger = 100
    cheeseburger = 70
    total = 0
    while True:
        print("    BURGERS")
        print()
        print("(1) Big Mac - ₱150")
        print("(2) LycCrispy Chicken Sandwich - ₱130")
        print("(3) LycSpicy Chicken Sandwich - ₱100")
        print("(4) Double Cheeseburger - ₱100")
        print("(5) Cheeseburger Meal - ₱70")
        print()
        burgerMenuChoice = input("Choice: ")

        if (burgerMenuChoice == "1"):
            print("Order: Big Mac")
            quantity = int(input("Quantity: "))
            total += quantity * bigmac
            print("Total:" + str(total))
            break
        elif (burgerMenuChoice == "2"):
            print("Order: LycCrispy Chicken Sandwich")
            quantity = int(input("Quantity: "))
            total += quantity * crispyChicken
            print("Total:" + str(total))
            break
        elif (burgerMenuChoice == "3"):
            print("Order: LycSpicy Chicken Sandwich")
            quantity = int(input("Quantity: "))
            total += quantity * spicyChicken
            print("Total:" + str(total))
            break
        elif (burgerMenuChoice == "4"):
            print("Order: Double Cheeseburger")
            quantity = int(input("Quantity: "))
            total += quantity * dcheeseburger
            print("Total:" + str(total))
            break
        elif (burgerMenuChoice == "5"):
            print("Order: Cheeseburger Meal")
            quantity = int(input("Quantity: "))
            total += quantity * cheeseburger
            print("Total:" + str(total))
            break
        else:
            print("Invalid choice, please choose again")
            print()

#displays the fries meal menu section
def friesMealsMenu():
    ssfbbq = 70
    ssfc = 70
    fries = 50
    cms = 50
    cgs = 50
    total = 0
    while True:
        print("    FRIES AND ADD ONS")
        print()
        print("(1) Shake Shake Fries BBQ - ₱70")
        print("(2) Shake Shake Fries Cheese - ₱70")
        print("(3) Fries - ₱50")
        print("(4) Creamy Mushroom Soup - ₱50")
        print("(5) Creamy Garlic Soup - ₱50")
        print()
        friesMenuChoice = input("Choice: ")

        if (friesMenuChoice == "1"):
            print("Order: Shake Shake Fries BBQ")
            quantity = int(input("Quantity: "))
            total += quantity * ssfbbq
            print("Total:" + str(total))
            break
        elif (friesMenuChoice == "2"):
            print("Order: Shake Shake Fries Cheese")
            quantity = int(input("Quantity: "))
            total += quantity * ssfc
            print("Total:" + str(total))
            break
        elif (friesMenuChoice == "3"):
            print("Order: Fries")
            quantity = int(input("Quantity: "))
            total += quantity * fries
            print("Total:" + str(total))
            break
        elif (friesMenuChoice == "4"):
            print("Order: Creamy Mushroom Soup")
            quantity = int(input("Quantity: "))
            total += quantity * cms
            print("Total:" + str(total))
            break
        elif (friesMenuChoice == "5"):
            print("Order: Creamy Garlic Soup")
            quantity = int(input("Quantity: "))
            total += quantity * cgs
            print("Total:" + str(total))
            break
        else:
            print("Invalid choice, please choose again")
            print()

#displays the beverage meal menu section
def beverageMealsMenu():
    lfo = 50
    lf = 50
    sundae = 30
    icet = 30
    orangej = 30
    coke = 30
    sprite = 30
    total = 0
    while True:
        print("    BEVERAGES")
        print()
        print("(1) LycFlurry Oreo - ₱50")
        print("(2) LycFloat - ₱50")
        print("(3) Sundae - ₱30")
        print("(4) Iced Tea - ₱30")
        print("(5) Orange Juice - ₱30")
        print("(6) Coke - ₱30")
        print("(7) Sprite - ₱30")
        print()
        beverageMenuChoice = input("Choice: ")

        if (beverageMenuChoice == "1"):
            print("Order: LycFlurry Oreo")
            quantity = int(input("Quantity: "))
            total += quantity * lfo
            print("Total:" + str(total))
            break
        elif (beverageMenuChoice == "2"):
            print("Order: LycFloat")
            quantity = int(input("Quantity: "))
            total += quantity * lf
            print("Total:" + str(total))
            break
        elif (beverageMenuChoice == "3"):
            print("Order: Sundae")
            quantity = int(input("Quantity: "))
            total += quantity * sundae
            print("Total:" + str(total))
            break
        elif (beverageMenuChoice == "4"):
            print("Order: Iced Tea")
            quantity = int(input("Quantity: "))
            total += quantity * icet
            print("Total:" + str(total))
            break
        elif (beverageMenuChoice == "5"):
            print("Order: Orange Juice")
            quantity = int(input("Quantity: "))
            total += quantity * orangej
            print("Total:" + str(total))
            break
        elif (beverageMenuChoice == "6"):
            print("Order: Coke")
            quantity = int(input("Quantity: "))
            total += quantity * coke
            print("Total:" + str(total))
            break
        elif (beverageMenuChoice == "7"):
            print("Order: Sprite")
            quantity = int(input("Quantity: "))
            total += quantity * sprite
            print("Total:" + str(total))
            break
        else:
            print("Invalid choice, please choose again")
            print()

#displays the pasta meal menu section
def pastaMealsMenu():
    css = 100
    rc = 100
    total = 0
    while True:
        print("    PASTA")
        print()
        print("(1) Creamy Sweet Spaghetti - ₱100")
        print("(2) Ricotta Carbonara - ₱100")
        print()
        pastaMenuChoice = input("Choice: ")

        if (pastaMenuChoice == "1"):
            print("Order: Creamy Sweet Spaghetti")
            quantity = int(input("Quantity: "))
            total += quantity * css
            print("Total:" + str(total))
            break
        elif (pastaMenuChoice == "2"):
            print("Order: Ricotta Carbonara")
            quantity = int(input("Quantity: "))
            total += quantity * rc
            print("Total:" + str(total))
            break
        else:
            print("Invalid choice, please choose again")
            print()

start()
dinePlace()
print()
