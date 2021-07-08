# constants
MIN_ITEMS = 4       # minimum number of items
MAX_ITEMS = 6       # maximum number of items
SALES_TAX = 0.12    # 12% sales tax
DISC_5_PER = 0.05   # 5% discount percentage
DISC_5_AMT = 10000  # minimum amount needed for 5% discount
DISC_3_PER = 0.03   # 3% discount percentage
DISC_3_AMT = 8000   # minimum amount needed for 3% discount
WARNING_AMT = 100   # warning amount (warn user if item < 100)

# variables
item1 = "Laptop"        # item choice 1
item2 = "TV"            # item choice 2
item3 = "Game Console"  # item choice 3
item4 = "Cell Phone"    # item choice 4
item5 = "Speaker"       # item choice 5
item6 = "Camera"        # item choice 6

userInput = ""          # string to compare user input (if statement)
validNumber = False     # while loop condition
items = 0               # item number accumulator 

laptop = 0.0        # price of laptop (item1)
tv = 0.0            # price of tv (item2)
gameConsole = 0.0   # price of game console (item3)
cellPhone = 0.0     # price of cell phone (item4)
speaker = 0.0       # price of speaker (item5)
camera = 0.0        # price of camera (item6)

running_total= 0.0  # running total while item prices are being entered
subtotal = 0.0      # total price of all selected items
tax_total = 0.0     # total with tax (before discount)
discount = 0.0      # discount applied dollar amount
disc_total = 0.0    # total with discount applied
final_total = 0.0   # final total with tax and discount (if applicable)


# program output header
print("\nWelcome to the Electronics Store's receipt program!\n")
# prompt for beginning user input
print("Items bought:")
# notify user how to select an item
print("(Enter 'y' or 'Y' if the item below was purchased)")
# user input for item selection
userInput = input(f"\n{item1}? ")
# compare user input for validation
if userInput == "y" or userInput == "Y":
    # while validNumber is false, loop will reiterate
    while not validNumber:
        # test to see if input is a number
        try:
            # user input for item price
            laptop = float(input(f"Enter {item1} price: "))
            # if input is a number, validNumber is true and program continues
            validNumber = True
        except:
            # re-prompt user to enter a numerical value
            print("\nPlease enter the sales price in numbers.\n")
    # add 1 to items to keep count of number of items
    items += 1
    # add price of item to running_total
    running_total += laptop
    # if item is less than $100
    if laptop <= WARNING_AMT:
        # warn user that the price entered is less than $100
        print(f"\nYou have entered {laptop} which is less than/equal to {WARNING_AMT}.")
        # if price is correct, user can continue. If price is wrong, user must start over
        print("If this price is correct, continue with the program.")
# if userInput does not equal y or Y, item will not be counted                           
else:
    print(f"\n{item1} will not be included in the receipt.")
# reset while loop condition for other items
validNumber = False

# COMMENTS FOR LINES 78 - 116 ARE THE SAME AS COMMENTS FROM LINES 44 - 73

userInput = input(f"\n{item2}? ")
if userInput == "y" or userInput == "Y":
    while not validNumber:
        try:
            tv = float(input(f"Enter {item2} price: "))
            validNumber = True
        except:
            print("\nPlease enter the sales price in numbers.\n")
    items += 1
    running_total += tv
    if tv <= WARNING_AMT:
        print(f"\nYou have entered {tv} which is less than/equal to {WARNING_AMT}.")
        print("If this price is correct, continue with the program.")                     
else:
    print(f"\n{item2} will not be included in the receipt.")

validNumber = False

# COMMENTS FOR LINES 101 - 119 ARE THE SAME AS COMMENTS FROM LINES 78 - 116

userInput = input(f"\n{item3}? ")
if userInput == "y" or userInput == "Y":
    while not validNumber:
        try:
            gameConsole = float(input(f"Enter {item3} price: "))
            validNumber = True
        except:
            print("\nPlease enter the sales price in numbers.\n")
    items += 1
    running_total += gameConsole
    if gameConsole <= WARNING_AMT:
        print(f"\nYou have entered {gameConsole} which is less than/equal to {WARNING_AMT}.")
        print("If this price is correct, continue with the program.")                    
else:
    print(f"\n{item3} will not be included in the receipt.")

validNumber = False

# COMMENTS FOR LINES 124 - 142 ARE THE SAME AS COMMENTS FROM LINES 101 - 119

userInput = input(f"\n{item4}? ")
if userInput == "y" or userInput == "Y":
    while not validNumber:
        try:
            cellPhone = float(input(f"Enter {item4} price: "))
            validNumber = True
        except:
            print("\nPlease enter the sales price in numbers.\n")
    items += 1
    running_total += cellPhone
    if cellPhone <= WARNING_AMT:
        print(f"\nYou have entered {cellPhone} which is less than/equal to {WARNING_AMT}.")
        print("If this price is correct, continue with the program.")                      
else:
    print(f"\n{item4} will not be included in the receipt.")

validNumber = False

# COMMENTS FOR LINES 147 - 165 ARE THE SAME AS COMMENTS FROM LINES 124 - 142

userInput = input(f"\n{item5}? ")
if userInput == "y" or userInput == "Y":
    while not validNumber:
        try:
            speaker = float(input(f"Enter {item5} price: "))
            validNumber = True
        except:
            print("\nPlease enter the sales price in numbers.\n")
    items += 1
    running_total += speaker
    if speaker <= WARNING_AMT:
        print(f"\nYou have entered {speaker} which is less than/equal to {WARNING_AMT}.")
        print("If this price is correct, continue with the program.")                     
else:
    print(f"\n{item5} will not be included in the receipt.")

validNumber = False

# COMMENTS FOR LINES 170 - 186 ARE THE SAME AS COMMENTS FROM LINES 147 - 165

userInput = input(f"\n{item6}? ")
if userInput == "y" or userInput == "Y":
    while not validNumber:
        try:
            camera = float(input(f"Enter {item6} price: "))
            validNumber = True
        except:
            print("\nPlease enter the sales price in numbers.\n")
    items += 1
    running_total += camera
    if camera <= WARNING_AMT:
        print(f"\nYou have entered {camera} which is less than/equal to {WARNING_AMT}.")
        print("If this price is correct, continue with the program.")                      
else:
    print(f"\n{item6} will not be included in the receipt.")

# number of items must be between 4 and 6
if items >= MIN_ITEMS and items <= MAX_ITEMS:
    # subtotal is equal to the sum of all the item prices
    subtotal = running_total
    # tax total is the subtotal plus 12% of the subtotal
    tax_total = subtotal + subtotal * SALES_TAX
    # if the subtotal is greater than $10,000 then a 5% discount is applied
    if subtotal > DISC_5_AMT:
        # discount is equal to 5% of the subtotal
        discount = subtotal * DISC_5_PER
        # discount total is equal to the subtotal minus 5% of the subtotal
        disc_total = subtotal - discount
        # final total is equal to the discount total plus 12% of the discount total
        final_total = disc_total + disc_total * SALES_TAX
    else:
        # if the subtotal is greater than $8,000 but less than $10,000
        # then a 3% discount is applied
        if subtotal > DISC_3_AMT:
            # discount is equal to 3% of the subtotal
            discount = subtotal * DISC_3_PER
            # discount total is equal to the subtotal minus 3% of the subtotal
            disc_total = subtotal - discount
            # final total is equal to the discount total plus 12% of the discount total
            final_total = disc_total + disc_total * SALES_TAX
        else:
            # if the subtotal is less than 10,000 and 8,000 
            # then the tax total becomes the final total
            final_total = tax_total

# output to the user the items and their prices, the total before taxes,
# the total after taxes, and the total after the discount is applied (if applicable)
print(f"\n{item1}: ${laptop:,.2f} \n{item2}: ${tv:,.2f} \n{item3}: ${gameConsole:,.2f}"
      + f"\n{item4}: ${cellPhone:,.2f} \n{item5}: ${speaker:,.2f} \n{item6}: ${camera:,.2f}"
      + f"\nSubtotal: ${subtotal:,.2f} \nTotal with taxes: ${tax_total:,.2f}"
      + f"\nTotal after discount: ${final_total:,.2f}")

