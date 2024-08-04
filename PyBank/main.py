#This will allow us to create file path across operating systems
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row
    csv_header = next(csvfile)

    # Initialize variables for total months, total profit, and max and min profit
    total_months = 0
    total_revenue = 0
    revenue = 0
    change_in_revenue = 0
    previous_revenue = 0
    max_change_in_revenue = float('-inf')
    min_change_in_revenue = float('inf')
    max_change_month = ""
    min_change_month = ""

    #Loop through each row in the CSV file
    for row in csvreader:

        # Calculate the number of months
        total_months += 1
        
        #Calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row[1])
 
        # Calculate the revenue change for each month
        if previous_revenue!= 0:
            change_in_revenue = int(row[1]) - previous_revenue
            if change_in_revenue > max_change_in_revenue:
                max_change_in_revenue = change_in_revenue
                max_change_month = row[0]
            elif change_in_revenue < min_change_in_revenue:
                min_change_in_revenue = change_in_revenue
                min_change_month = row[0]
               
        # Calculate the average change in revenue
        change_in_revenue += int(row[1]) - previous_revenue
        average_change_in_revenue = change_in_revenue / total_months if total_months > 0 else 0
    
        # Update the previous revenue
        previous_revenue = int(row[1])
   
    #Print the results
    print("Financial Analysis:")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_revenue}")
    print(f"Average Change: ${round(average_change_in_revenue, 2)}")
    print(f"Greatest Increase in Profit: {max_change_month} (${max_change_in_revenue})")
    print(f"Greatest Decrease in Profit: {min_change_month} (${min_change_in_revenue})")