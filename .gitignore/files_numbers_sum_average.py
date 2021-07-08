# This program reads all the values in a file and
# calculates the average and sum of all values read.

def main():
    # Define variables for calculation
    num_sum = 0.0
    num_avg = 0.0
    running_total = 0.0
    count = 0
    # Open numbers.txt in read mode
    num_file = open("numbers.txt", "r")
    print("Numbers in File\n---------------")
    # Read all lines from numbers.txt
    for line in num_file:
        # Convert line to float for calculations
        value = float(line)
        # Format and output line to user
        print(f"{value:,.2f}")
        # Add value to running total
        running_total += value
        # Keep count of number of lines
        count += 1

    # Close file
    num_file.close()
    # Transfer running total to sum for calculations
    num_sum = running_total
    # Divide sum by # of lines
    num_avg = num_sum / count
    # Output sum and average to user
    print(f"\nFile SUM: {num_sum:,.2f} " +
          f"\nFile AVERAGE: {num_avg:,.2f}")

# Call main function
main()
