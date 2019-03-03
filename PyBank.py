#Import Dependencies perform certain functions in python
import os
import csv

# define where the data is located
bankcsv = os.path.join("Resources", "budget_data.csv")

# define empty lists for Date, profit/loss and profit and loss changes
Profit_loss = []
Date = []
PL_Change = []

# Read csv file
with open(bankcsv, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

# calculate the values for the profit/loss and the dates
# store respective values in appropraite lists created earlier    
    for row in csvreader:
        Profit_loss.append(float(row[1]))
        Date.append(row[0])

#Print the calculated values
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {len(Date)}")
print(f"Total Revenue: {sum(Profit_loss)}")
#Calculate the average revenue change, the greatest revenue increase and the greatest revenue decrease 
for i in range(1,len(Profit_loss)):
        PL_Change.append(Profit_loss[i] - Profit_loss[i-1])   
        avg_PL_Change = (sum(PL_Change)/len(PL_Change))

        max_PL_Change = max(PL_Change)

        min_PL_Change = min(PL_Change)

        max_PL_Change_date = str(Date[PL_Change.index(max(PL_Change)) + 1])
        min_PL_Change_date = str(Date[PL_Change.index(min(PL_Change)) + 1])
# print the calculated values
print(f"Avereage Revenue Change: {round(avg_PL_Change,2)}")
print(f"Greatest Increase in Revenue: {max_PL_Change_date}, {max_PL_Change}")
print(f"Greatest Decrease in Revenue: {min_PL_Change_date}, {min_PL_Change}") 

#export text file
p = open("PyBank.txt","w+")  
p.write("Financial Analysis\n")
p.write("-----------------------------------\n")  
p.write(f"Total Months: {len(Date)}\n")    
p.write(f"Total Revenue: {sum(Profit_loss)}\n")
p.write(f"Avereage Revenue Change: {round(avg_PL_Change,2)}\n")
p.write(f"Greatest Increase in Revenue: {max_PL_Change_date}, {max_PL_Change}\n")
p.write(f"Greatest Decrease in Revenue: {min_PL_Change_date}, {min_PL_Change}\n")
p.close()
