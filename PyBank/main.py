# Dependencies 
import os
import csv 

# find path
budget_data = os.path.join("resources","PyBank","budget_data.csv")

# create empty lists
total_months = []
total_profit = []
revenue_change = []


# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
  
 

    # go through each row
    for row in csvreader:
       
        # append total number of months and profit
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # iterate through profits to get monthly change in proftis 
    for i in range(len(total_profit)-1):

        # take differences
        revenue_change.append(total_profit[i+1]-total_profit[i])

# get max and min value
max_increase = max(revenue_change)
max_decrease = min(revenue_change)   

# get max and min month
max_increase_month = total_profit.append(max(revenue_change))+1
max_decrease_month = total_profit.append(min(revenue_change))+1

length1 = len(total_months)
sum1 = sum(total_profit)
average_change = {round(sum(revenue_change)/len(revenue_change),2)}
increase_date = total_months[max_increase_month]
decrease_date = total_months[max_decrease_month]



# print statements 
output = "Finanacial Analysis" + "\n" + "--------------------------------------------\n" + "Total Months: " + str(length1) + "\n" + "Total Profit: $" +  str(sum1) + "\n" + "Average Change: " + str(average_change) + "\n" + "Greatest Increase in Profits: " + str(increase_date) + "$" + str(max_increase) + "\n" + "Greatest Decrease in Profits: " + str(decrease_date) + "$" + str(max_decrease)
print(output)  

outfile = open("output.txt","w")