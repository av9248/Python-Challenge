#This will allow us to create file path across operating systems
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row
    csv_header = next(csvreader)

    # Initialize variables for total months, total profit, and max and min profit
    total_months = 0
    total_profit_losses = 0
    change_in_profit_losses = 0
    list_profit_losses = []
    average_change_in_profit_losses = 0
    current_profit_loss_row = 0
    greatest_increase_profit_loss = ["",0]
    greatest_decrease_profit_loss = ["",9999999999999999999]

    # Get the profit loss from the second row (the first row is the header)
    previous_profit_loss_row = int(next(csvreader)[1])

    # Loop through each row in the CSV file
    for row in csvreader:

        #Total months count
        total_months = total_months + 1

        #calculate total profit loss
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

        #Find the greatest increase in profits 
        

    #Print the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change_in_profit_losses:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_profit_loss[0]} (${greatest_increase_profit_loss[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_profit_loss[0]} (${greatest_decrease_profit_loss[1]})")

    