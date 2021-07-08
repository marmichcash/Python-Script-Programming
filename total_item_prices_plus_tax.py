# A customer is purchasing 5 items.
# The items are entered through the keyboard using the Input Function.
# The program will calculatethe Subtotal, sales tax, and total.
# Assume the sales tax is 7% (can be Written as TAX_RATE = 0.07)
# The program displays/output the items, subtotal, SalesTax, and the Total for the output.

# Define Variables
# Holds prices of items, subtotal, tax rate, sales tax, and total
item1 = 0.0
item2 = 0.0
item3 = 0.0
item4 = 0.0
item5 = 0.0
subtotal = 0.0
TAX_RATE = 0.07
salesTax = 0.0
total = 0.0

# Get input for the price of each item
item1 = float(input("Enter the price of item #1: "))
item2 = float(input("Enter the price of item #2: "))
item3 = float(input("Enter the price of item #3: "))
item4 = float(input("Enter the price of item #4: "))
item5 = float(input("Enter the price of item #5: "))

# Calculate subtotal of items
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate sales tax from subtotal with given tax rate
salesTax = subtotal * TAX_RATE

# Calculate overall total of items and sales tax
total = subtotal + salesTax

# Print the price of each item, subtotal, sales tax, and overall total
print(f"Item #1: ${item1:.2f} \nItem #2: ${item2:.2f} \nItem #3: ${item3:.2f}" +
      f"\nItem #4: ${item4:.2f} \nItem #5: ${item5:.2f} \n\nSubtotal: ${subtotal:.2f}" +
      f"\nSales Tax: ${salesTax:.2f} \nTotal: ${total:.2f}")
