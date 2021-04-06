# Import the os module and module for reading CSV files
import os
import csv

# Path for the csv file
budget_Data = os.path.join('Resources','budget_data.csv')

# Lists to store Data
Months = []
Profit_Losses = []
#Total_Change = []


# Variable initialisation
Total_Months = 0
Total_Revenue = 0
Average_Change = 0



# Open the CSV
with open(budget_Data, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csv_reader)

    for row in csv_reader:
        
        Months.append (row[0])
        Profit_Losses.append (row[1])

        # Calculate Total Months
        Total_Months= len (Months)
        ##print (Total_Month)

        # Calculate the Total
        Total_Revenue = Total_Revenue + int (row[1])
        ##print (Total_Revenue)
        
        #Calculate the changes in "Profit/Losses" over the entire period
        Total_Change = []

        i=0
        for i in range(Total_Months - 1):
            Monthly_Change = int(Profit_Losses[i+1]) - int(Profit_Losses[i])
            Total_Change.append (Monthly_Change)
 
            Sum_Change = sum(Total_Change)

            #The average of the changes
            Average_Change = Sum_Change / Total_Months
            Average_Change = round(Average_Change, 2)


            #Date and amount of the greatest increase in profits
            Greatest_Increase_in_Profits = max(Total_Change)
            Greatest_Increase_Date = Months[Total_Change.index(Greatest_Increase_in_Profits)]
        
            #Date and amount of the greatest decrease in profits
            Greatest_Decrease_in_Profits = min(Total_Change)
            Greatest_Decrease_Date = Months[Total_Change.index(Greatest_Decrease_in_Profits)]
        
    #Print the analysis to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+ str(Total_Months))
    print("Total: $"+ str(Total_Revenue))
    print("Average Change: $"+ str(Average_Change))
    print("Greatest Increase in Profits:"+ str(Greatest_Increase_Date)+" ($"+ str(Greatest_Increase_in_Profits)+")")
    print("Greatest Increase in Profits:"+ str(Greatest_Decrease_Date)+" ($"+ str(Greatest_Decrease_in_Profits)+")")

#Export a text file with the results
with open('Financial_Analysis', 'w') as textfile:
    print("Financial Analysis", file=textfile)
    print("----------------------------", file=textfile)
    print("Total Months: "+ str(Total_Months), file=textfile)
    print("Total: $"+ str(Total_Revenue), file=textfile)
    print("Average Change: $"+ str(Average_Change), file=textfile)
    print("Greatest Increase in Profits:"+ str(Greatest_Increase_Date)+" ($"+ str(Greatest_Increase_in_Profits)+")", file=textfile)
    print("Greatest Increase in Profits:"+ str(Greatest_Decrease_Date)+" ($"+ str(Greatest_Decrease_in_Profits)+")", file=textfile)
    