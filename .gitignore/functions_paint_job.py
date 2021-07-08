def main():
    # local variables
    job_sqft = 0.0          # number of square feet
    job_gal_price = 0.0     # price per gallon
    job_gal = 0.0           # number of gallons
    job_hrs = 0.0           # labor needed in hours
    job_cost_p = 0.0        # total price of paint
    job_cost_l = 0.0        # total price of labor
    job_total = 0.0         # overall job cost   
    job_sqft, job_gal_price = get_input()
    job_gal = calc_num_gallons(job_sqft)
    job_hrs = calc_req_labor(job_gal)
    job_cost_p = calc_paint_cost(job_gal, job_gal_price)
    job_cost_l = calc_labor_cost(job_hrs)
    job_total = calc_total_job(job_cost_p, job_cost_l)
    print_job(job_gal, job_hrs, job_cost_p, job_cost_l, job_total)
# gets the square feet and gallon price from user
def get_input():
    sqft = float(input("Enter the square feet of wall space to be painted: "))
    gal_price = float(input("Enter the price of paint per gallon: "))
    return sqft, gal_price
# calculates number of gallons of paint needed to cover square feet
def calc_num_gallons(sqft):
    one_gallon = 112        # one gallon covers 112 square feet of wall space
    num_gallons = 0.0
    num_gallons = sqft / one_gallon
    return num_gallons
# calculates labor (in hours) required to paint
def calc_req_labor(num_gallons):
    labor_per_gal = 8.0     # hours of labor for each gallon of paint
    labor_hrs = 0.0
    labor_hrs = num_gallons * labor_per_gal
    return labor_hrs

# calculates the total cost of paint
def calc_paint_cost(num_gallons, gal_price):
    paint_cost = 0.0
    paint_cost = num_gallons * gal_price
    return paint_cost

# calculates the total cost of labor
def calc_labor_cost(labor_hrs):
    charge = 35.00      # price per hour of labor
    labor_cost = 0.0
    labor_cost = charge * labor_hrs
    return labor_cost

# calculates the total cost of the entire job
def calc_total_job(paint_cost, labor_cost):
    total = 0.0
    total = paint_cost + labor_cost
    return total

# prints the square feet, paint price per gallon, gallons of paint,
# hours of labor, paint and labor charges, and total job cost
def print_job(num_gallons, labor_hrs, paint_cost, labor_cost, total):
    print(f"Gallons of paint: {num_gallons:.1f} \nHours of labor: {labor_hrs:.1f}"
          + f"\nPaint charges: ${paint_cost:.2f} \nLabor Charges: ${labor_cost:.2f}"
          + f"\nTotal cost: ${total:.2f}")
    
# start the program
main()

