#Importing relevant modules
import csv
import os

#Create the file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Opens the file that is specified by the file path and tells us that we are working within this file
with open(csvpath) as csvfile:
    
    #Read the file with a specified delimiter, which is a comma
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip the header
    next(csvreader)
    
    MonthCount = 0 #Inititalize a counter
    NetAmount = 0 #Inititalize total amount
    GreatestIncrease = 0
    GreatestDecrease = 0
    Change = [] #Inititalize a dynamic array to keep track of changes
    int(MonthCount)
    #Loops through each row in the file, starting with the data row
    for row in csvreader:
        
        #counts the number of entries there are by using a counter that adds for every loop
        MonthCount = MonthCount + 1
        
        #cumulatively adds the profits and losses after reading each row
        #Must make it a float as csv files are read as strings
        NetAmount = float(row[1]) + NetAmount
        
        #start keeping track of changes at the 2nd entry, 
        #initialize the starting amount at the 1st entry
        if MonthCount == 1:
            PreviousAmount = float(row[1])
        else:
            MonthlyChange = float(row[1]) - PreviousAmount
            Change.append(MonthlyChange)
            PreviousAmount = float(row[1])
            
            #Check each change if it is greater than the previouys change,
            #if it is true, then we store that greatest change until it needs to be
            #overwritten again. This is similar to Decrease
            
            if MonthCount >= 3:
                if GreatestIncrease < Change[MonthCount-2]:
                    GreatestIncrease = Change[MonthCount-2]
                    GreatestIncreaseDate = row[0]
                elif GreatestDecrease > Change[MonthCount-2]:
                    GreatestDecrease = Change[MonthCount-2]
                    GreatestDecreaseDate = row[0]
        
        

    AvgChange = round(sum(Change)/(len(Change)),2)       
    NetAmount = round(NetAmount)
    financial_analysis = {
        "Total Months": MonthCount,
        "Total": NetAmount,
        "Average Change": AvgChange,
        "Greatest Increase in Profits": [GreatestIncreaseDate, GreatestIncrease],
        "Greatest Decrease in Profits": [GreatestDecreaseDate, GreatestDecrease]}
    
    print(f' Total Months: {MonthCount}')
    print(f' Total: ${round(NetAmount)}')
    print(f' Average Change: ${round(AvgChange,2)}')
    print(f' Greatest Increase in Profits: {GreatestIncreaseDate} (${GreatestIncrease})' )
    print(f' Greatest Decrease in Profits: {GreatestDecreaseDate} (${GreatestDecrease})' )

#export to textfile

output_file = os.path.join("analysis", "Financial_Analysis.txt")

with open(output_file, "w") as txtfile:
    
    
    txtfile.writelines("Financial Analysis\n")
    txtfile.writelines("----------------------\n")
    txtfile.writelines(f' Total Months: {MonthCount}\n')
    txtfile.writelines(f' Total: ${round(NetAmount)}\n')
    txtfile.writelines(f' Average Change: ${round(AvgChange,2)}\n')
    txtfile.writelines(f' Greatest Increase in Profits: {GreatestIncreaseDate} (${GreatestIncrease}n)\n' )
    txtfile.writelines(f' Greatest Decrease in Profits: {GreatestDecreaseDate} (${GreatestDecrease})\n' )