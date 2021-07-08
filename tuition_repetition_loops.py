# A college is increasing its tuition of $8,000 by 3% each year for 7 years.
# This program displays the projected tuition amount for the next 7 years.

# Constants
YEARLY_INCREASE = .03
NUM_INCREASES = 7

# Variables
tuition = 8000
current_year = 1

# While loop for yearly tuition increases
while current_year <= NUM_INCREASES:
    # Nested loop to keep loop from continuing past 7 (infinite loop) 
    if current_year <= NUM_INCREASES:
        # tuition is increased by 3% (basically tuition = tuition * 1.03)
        tuition += (tuition*(YEARLY_INCREASE))
        # Output the new year's tuition cost
        print(f"In {current_year} year(s), the tuition will be ${tuition:.2f}.")
        # Increment current_year + 1 for next year's tuition
        current_year += 1
    else:
        # If current_year is not <= 7, loop ends
        break
