# Write a program that will ask the user to enter the purchase price of three items.
# The program will compute the subtotal and total. Assume that the tax is 9 percent.
# The program runs and if the total is greater than $5000, the program gives a discount of 5% and 3% if the total is greater $3000.
# The program should display the cost of each item purchased, the subtotal, total with tax, the discount provided on the total, the total with the discount.

# Define constants
SALES_TAX = 0.09
DISCOUNT_5 = 0.05   # discount applied if total > $5000
DISCOUNT_3 = 0.03   # discount applied if $5000 > total > $3000

# Define variables
item1 = 0.0
item2 = 0.0
item3 = 0.0
subtotal = 0.0
tax = 0.0
total = 0.0
discount = 0.0
disc_total = 0.0    # total after discount

# Input for prices of items and convert string to float
item1 = float(input("Enter price of item #1: "))
item2 = float(input("Enter price of item #2: "))
item3 = float(input("Enter price of item #3: "))

# Calculate subtotal
subtotal = item1 + item2 + item3

# Calculate tax
tax = subtotal * SALES_TAX

# Calculate total with tax
total = subtotal + tax

# Determine if total is greater than $5000
if total > 5000:
    
    # Calculate discount of 5% from total
    discount = subtotal * DISCOUNT_5

    # Calculate total with discount
    disc_total = total - discount

else:
# Determine is total is greater than $3000
    if total > 3000:

        # Calculate discount of 3% from total
        discount = subtotal * DISCOUNT_3

        # Calculate total with discount
        disc_total = total - discount
    else:
        # No discount is applied, total remains the same
        disc_total = total

# Output price of items, subtotal, total, discount, and total with discount
print(f"Item #1: ${item1:.2f} \nItem #2: ${item2:.2f} \nItem #3: ${item3:.2f}"
      + f"\nSubtotal: ${subtotal:.2f} \nTotal with tax: ${total:.2f}"
      + f"\nDiscount: ${discount:.2f} \nTotal after discount: ${disc_total:.2f}")
