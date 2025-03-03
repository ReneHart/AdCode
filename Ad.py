#Declare Variables
#from datetime import date

#CustID = 0
#Store_string= "ABCD"
#TrasID = 0

# Import necessary modules
#import pandas as pd

# Transaction data
TransDate = [3, 6, 9, 14]

# Calculate total and average
Amount = sum(TransDate)
avg = Amount / len(TransDate)

# Print the average with two decimal places
print(f"The average for the month is: {avg:.2f}")

# Print transactions above the average
print("Transactions above the average:")
for number in TransDate:
    if number > avg:
        print(f"{number:.2f}")
