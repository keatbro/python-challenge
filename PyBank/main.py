# Import dependencies
import os
import csv

# Set initial variable values
total_months = 0
net_total = 0
previousRev = 0
monthly_change = []
dateList = []

# Set file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open csv file
with open(csvpath, newline='', encoding = 'UTF-8') as csvfile:
    
    # Read csv
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header
    csvheader = next(csvreader)
            
    # Iterate through rows in the file to calculate stats
    for row in csvreader:

       # Count the rows to get total months
       total_months = total_months + 1 
       
       # Sum the profit column to get net total
       net_total += int(row[1])

       # Calculate the difference between month profits
       monthDiff = float(row[1]) - previousRev
       previousRev = float(row[1])

       # Add differences to list
       monthly_change.append(monthDiff)

# Calculate average monthly change
avgMonthlyChange = round(sum(monthly_change) / len(monthly_change))

# Calculate min and max monthly change
# Turn values to integers
maxChange = int(max(monthly_change))
minChange = int(min(monthly_change))

# Associate the max and min changes to the correct date
# Get the index of the max and min
# Turn the dates in the csv into a list which you can index
maxIndex = monthly_change.index(max(monthly_change))
minIndex = monthly_change.index(min(monthly_change))

with open(csvpath, newline='', encoding = 'UTF-8') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader2)

    for date in csvreader2:
        dateList.append(date[0])

maxChangeMonth = dateList[maxIndex]
minChangeMonth = dateList[minIndex]

# Print statistics to the terminal
stats = (
 f'Financial Analysis \n'
 f'--------------------- \n'
 f'Total Months: {total_months} \n'
 f'Total: ${net_total} \n'
 f'Average Change: ${avgMonthlyChange} \n'
 f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange}) \n'
 f'Greatest Decrease in Profits: {minChangeMonth} (${minChange}) \n'
)

print(stats)

# Output a text file with the results
textFile = os.path.join('text.txt')
with open(textFile, 'w') as myFile:
    writer = myFile.write(stats)


