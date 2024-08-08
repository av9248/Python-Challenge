#This will allow us to create file path across operating systems
import os

#Module for reading CSV files
import csv

# Path to the CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Initialize variables for total months, total profit, and max and min profit
    total_months = 1
    list_profit_losses = []
    previous_profit_loss_row = 0
    greatest_increase_profit_loss = ["", 0]
    greatest_decrease_profit_loss = ["", 999999999999999]
    
    #Read the header row
    csv_header = next(csvreader)
    
    #Read the first row to get the initial profit loss
    previous_profit_loss_row = int(next(csvreader)[1])
    total_profit_losses = previous_profit_loss_row # This is the initial profit loss

    # Loop through each row in the CSV file
    for row in csvreader:

        #Total months count
        total_months = total_months + 1
    
        #Calculate the total profit/losses
        total_profit_losses = total_profit_losses + int(row[1])

        #Calculate the change in profit loss for each month
        change_in_profit_losses = int(row[1]) - previous_profit_loss_row
        previous_profit_loss_row = int(row[1])
           
        #Add the change in profit loss to the list
        list_profit_losses.append(change_in_profit_losses)

        #Find the greatest increase in profits 
        if change_in_profit_losses > greatest_increase_profit_loss[1]:
            greatest_increase_profit_loss = [row[0], change_in_profit_losses]

        #Find the greatest decrease in profits
        if change_in_profit_losses < greatest_decrease_profit_loss[1]:
            greatest_decrease_profit_loss = [row[0], change_in_profit_losses]
        
        
    # Calculate the average change in profit loss
    average_change_in_profit_losses = sum(list_profit_losses) / len(list_profit_losses)

    #Print the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change_in_profit_losses:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_profit_loss[0]} (${greatest_increase_profit_loss[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_profit_loss[0]} (${greatest_decrease_profit_loss[1]})")

    # Create a text file with the results
    txtpath ='Analysis/financial_analysis.txt'
    with open(txtpath, "w") as text_file:
        text_file.write("Financial Analysis\n")
        text_file.write("----------------------------\n")
        text_file.write(f"Total Months: {total_months}\n")
        text_file.write(f"Total: ${total_profit_losses}\n")
        text_file.write(f"Average Change: ${average_change_in_profit_losses:.2f}\n")
        text_file.write(f"Greatest Increase in Profits: {greatest_increase_profit_loss[0]} (${greatest_increase_profit_loss[1]})\n")
        text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_profit_loss[0]} (${greatest_decrease_profit_loss[1]})")


